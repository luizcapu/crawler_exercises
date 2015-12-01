url_gather
============

GOALS (Brazilian Portuguese)
-

Imagine que você quer coletar as páginas de um site e para cada página encontrar o conteúdo
textual das notícias dele.
Seu objetivo é implementar um coletor web que dada uma URL inicial (​
http://g1.com.br​
 por
exemplo) baixe todas os links contidos nela e depois baixe os links nessas páginas e assim por
diante. E para cada página execute a função do item anterior retornando o conteúdo textual da
notícia. Se você não escolheu fazer a questão ​
2) ​
use uma função/classe dummy no lugar da
extração do texto.

A profundidade da coleta deve ser parametrizável. Por exemplo, se a profundidade for igual a 0
você deve baixar apenas a URL inicial. Profundidade igual a 1 deve baixar a URL inicial e as
páginas linkadas a partir dela. E assim por diante.

Idealmente o processamento a ser feito em cada página deve ser customizável, ou seja, se eu
quiser usar outro algoritmo para extrair páginas (ou qualquer outra coisa) o coletor deve poder
me permitir isso.
Por fim, o programa deve ser capaz de usar o máximo de recursos possíveis seja de IO (baixar
páginas) ou de CPU (processamento de uma página).

Duas dicas:
­ Baixar apenas links apontando para o mesmo domínio já é suficiente (e mais rápido)
­ Baixar apenas os links da primeira página já é suficiente.


SOLUTION (Brazilian Portuguese)
-



INSTALLATION
-

1) Be sure your environment is ready to run Python (2.7x) applications (https://www.python.org/about/gettingstarted/)

2) Recommended use of virtual environment (Brazilian Portuguese reference: https://osantana.me/ambiente-isolado-para-python-com-virtualenv/)

3) Run install.sh file found at the root of the project


HELP OUTPUT
-

```
usage: url_gather.py [-h] [-u URL] [-d DEPTH] [-w WORKERS]
                     [-ae ACCEPTABLE_ERRORS] [-o OUT] [-cf COLLECTOR_FILE]
                     [-cc COLLECTOR_CLASS]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Initial URL to gather
  -d DEPTH, --depth DEPTH
                        Gathering depth
  -w WORKERS, --workers WORKERS
                        Number of parallel workers
  -ae ACCEPTABLE_ERRORS, --acceptable_errors ACCEPTABLE_ERRORS
                        Max acceptable errors to continue execution
                        (-1=disabled)
  -o OUT, --out OUT     Folder to save output files
  -cf COLLECTOR_FILE, --collector_file COLLECTOR_FILE
                        Path to custom .py file to act as collector
  -cc COLLECTOR_CLASS, --collector_class COLLECTOR_CLASS
                        Class name of custom collector
```


USAGE EXAMPLE
-

```
cd url_gather
python url_gather.py -u http://g1.globo.com/ -d 1 -w 5 -o /tmp/
```

USING A CUSTOM COLLECTOR
-

```
python url_gather.py -u http://g1.globo.com/ -cf ./collectors/test_custom_collector.py -cc TestCustomCollector
```

IMPORTANT
-

Your custom collector code MUST OBEY the collector interface BUT MUST NOT INHERIT from it.

Collector interface can be found at [ROOT]/url_gather/collectors/collector_interface.py

