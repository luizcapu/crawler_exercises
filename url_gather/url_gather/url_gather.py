__author__ = 'luiz'

import argparse
from collectors.default_collector import DefaultCollector
import os
from multiprocessing import Pool, Semaphore, Manager
import time
from threading import Thread, Event
import traceback


class URLGather(object):

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get("url")

        if not self.url:
            raise Exception("No URL to gather")

        self.max_depth = kwargs.get("depth", 1)
        self.workers = kwargs.get("workers", 1)
        self.max_errors = kwargs.get("acceptable_errors", None)

        self.out = kwargs.get("out", "/tmp/")
        if not self.out.endswith("/"):
            self.out += "/"
        self.out += "url_gather/"
        if not os.path.exists(self.out):
            os.makedirs(self.out)

        self.collector_file = kwargs.get("collector_file")
        self.collector_class = kwargs.get("collector_class")
        self._load_collector()
        self._gathered_urls = set()

        # initiate multiprocessing resources
        self._pool = Pool(self.workers)
        self._semaphore = Semaphore(self.workers)
        self._manager = Manager()
        self._url_children = self._manager.dict()
        self._url_errors = self._manager.dict()
        self._url_events = {}
        print "loaded"

    def _load_collector(self):
        if self.collector_file:
            if os.path.isfile(self.collector_file):
                if self.collector_class:
                    # TODO load custom collector
                    pass
                else:
                    raise Exception("Undefined custom collector class name.")
            else:
                raise Exception("Custom collector file %s not found." % self.collector_file)
        else:
            self.collector = DefaultCollector

    def run(self):
        self._gather_url(self.url)
        self._pool.close()
        self._pool.join()

        if self._exceed_max_errors():
            error_log = "%serror.log" % self.out
            with open(error_log, "w+") as f:
                f.write(self._url_errors)
            print "REACHED MAX ERRORS. SEE %s FILE TO MORE DETAILS" % error_log

    def task_done(self, result):
        self._semaphore.release()

    def _exceed_max_errors(self):
        return self.max_errors is not None and self.max_errors >= 0 and len(self._url_errors) > self.max_errors

    def _wait_children_in_thread(self, url):
        while url not in self._url_children:
            time.sleep(0.1)
        event = self._url_events.pop(url)
        event.set()

    def _wait_for_children(self, url):
        event = Event()
        self._url_events[url] = event
        t = Thread(target=self._wait_children_in_thread, args=(url,))
        t.start()
        event.wait()

    def _gather_url(self, url, current_depth=0):
        if self._exceed_max_errors() or url in self._gathered_urls:
            return
        self._gathered_urls.add(url)

        gather_children = current_depth < self.max_depth

        self._semaphore.acquire()
        if self._exceed_max_errors():
            return
        self._pool.apply_async(
            run_in_child,
            (url, self.collector, self._url_children, gather_children, self.out, self._url_errors),
            callback=self.task_done
        )

        #  gather children links
        if gather_children:
            self._wait_for_children(url)
            if self._url_children[url]:
                for child in self._url_children[url]:
                    self._gather_url(child, current_depth+1)


def run_in_child(url, collector, url_children_map, gather_children, out, url_errors_map):
    max_tries = 5
    tries = 1  # try each url 5 times in case of errors
    while tries <= max_tries:
        try:
            print "Extracting URL %s (Try %i/%i)" % (url, tries, max_tries)
            collector_instance = collector(url)

            # load children only if needed
            if gather_children:
                url_children_map[url] = collector_instance.get_children_urls()

            out_name = url.split("/", 2)[2].replace("/", "_")
            with open("%s%s.out" % (out, out_name), "w+") as f:
                f.write(collector_instance.extract_content())
            return
        except:
            tries += 1
            if tries > max_tries:
                print traceback.format_exc()
                url_errors_map[url] = traceback.format_exc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Initial URL to gather")
    parser.add_argument("-d", "--depth", type=int, default=1, help="Gathering depth")
    parser.add_argument("-w", "--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("-ae", "--acceptable_errors", type=int, default=-1, help="Max acceptable errors to continue execution (-1=disabled)")
    parser.add_argument("-o", "--out", default="/tmp/", help="Folder to save output files")
    parser.add_argument("-cf", "--collector_file", help="Path to custom .py file to act as collector")
    parser.add_argument("-cc", "--collector_class", help="Class name of custom collector")
    args = parser.parse_args()

    args.url = "http://noticias.terra.com.br/"

    gather = URLGather(**args.__dict__)
    gather.run()

