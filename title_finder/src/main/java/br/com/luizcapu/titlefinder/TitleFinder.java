package br.com.luizcapu.titlefinder;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.TreeSet;

import org.apache.commons.lang3.StringUtils;

public class TitleFinder {
	
	private Path basePath;
	private String basePathStr;
	private List<String> titles;
	private Map<String, Object> wordInTitleMap;
	
	private static Set<String> stopWords;	
	private static String[] replacement = null;
	private static final String emptyStr = "";
	private static final String resourcesPath = "/src/main/resources/";
	private static final String defaultTitleFileName = "example.txt";
	private static final String stopWordsFileName = "stop_words.txt";	
	private static final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	private static final String[] toReplace = new String[]{",", ";", ".", "!", "?"};
	
	private static void printHelp() {
		println("You must pass the location of title txt file as UNIQUE argument");
	}
	
	private static void print(String value){
		System.out.print(value);
	}

	private static void println(String value){
		System.out.println(value);
	}
	
	public static void main(String[] args) throws IOException {
				
		String titleFile = (args.length == 1) ? args[0] : null;		
		
		if (titleFile == null) {
			print("Could not get title file from arguments. Do you wanna use default example file ? (Y/n): ");
			if (reader.readLine().trim().toLowerCase().equalsIgnoreCase("n")) {
				printHelp();
				return;
			}
		}
		
		TitleFinder finder = new TitleFinder(titleFile);
		String searchFor;
		while (!(searchFor = finder.askForSearch()).equalsIgnoreCase(emptyStr)) {
			Collection<Integer> titles = finder.searchWordInTitles(searchFor);
			
			long ini = System.currentTimeMillis();
			println(emptyStr);
			if (titles == null || titles.size() == 0) {
				println("No titles found for " + searchFor);
			} else {
				println(titles.size() + " title(s) found for " + searchFor);
				for (Integer titleID : titles){
					println(finder.translateTitleId(titleID));
				}
			}
			println("Response in: "+ (System.currentTimeMillis() - ini) +" ms"); 
			println(emptyStr);
		}
		println("END OF EXECUTION");
	}
	
	private String translateTitleId(Integer titleID) {
		return this.titles.get(titleID);
	}
	
	private void loadStopWords() throws IOException{
		if (stopWords == null) {
			stopWords = new TreeSet<String>();
			BufferedReader br = new BufferedReader(new FileReader(this.basePathStr + resourcesPath + stopWordsFileName));
			String word;
			while ((word = br.readLine()) != null) {
				stopWords.add(word);
			}
		}		
	}
	
	@SuppressWarnings("unchecked")
	private void parseTitleFile(String titleFile) throws IOException {
		if (titleFile == null) {
			titleFile = this.basePathStr + resourcesPath + defaultTitleFileName;
		}
		
		// load title file
		println("Waiting... Loading and parsing file " + titleFile);
		BufferedReader br = new BufferedReader(new FileReader(titleFile));
		String title;
		// parse lines and words
		while ((title = br.readLine()) != null) {
			
			int titleIdx = this.titles.size();
			this.titles.add(title);
			
			String[] words = title.split(" ");
			for (int w=0; w < words.length; w++) {
				String word = normalizeText(words[w]);
				// ignore if is a stop word or empty string
				if (word.equalsIgnoreCase(emptyStr) || stopWords.contains(word)){
					continue;
				}
				
				// add to map and inc frequency
				Map<Integer,Integer> wordTitles = (this.wordInTitleMap.containsKey(word)) ? (Map<Integer,Integer>) this.wordInTitleMap.get(word) : null;
				if (wordTitles == null) {
					wordTitles = new HashMap<Integer, Integer>();
					this.wordInTitleMap.put(word, wordTitles);
				}
				
				Integer frequency = wordTitles.get(titleIdx);
				frequency = (frequency == null) ? 1 : frequency + 1;
				wordTitles.put(titleIdx, frequency);
			}
		}
		
		// final parse wordMap ordering titleIDs by frequency
		for (Entry<String, Object> entry : this.wordInTitleMap.entrySet()) {
			this.wordInTitleMap.put(entry.getKey(), mapToOrderedSet((Map<Integer,Integer>) entry.getValue()));
		}
	}
	
	private static final Comparator<Entry<Integer, Integer>> mapComparator = new Comparator<Entry<Integer, Integer>>() {
	    public int compare(Entry<Integer, Integer> o1, Entry<Integer, Integer> o2) {
            return o1.getValue().compareTo(o2.getValue());
	    }
	};
	
	private List<Integer> mapToOrderedSet(Map<Integer, Integer> map) {
		List<Entry<Integer, Integer>> ordered = new LinkedList<Entry<Integer, Integer>>(map.entrySet());
		// sort by frequency
		Collections.sort(ordered, mapComparator);
		// reverse to print more relevant first
		Collections.reverse(ordered);
		
		List<Integer> result = new ArrayList<Integer>();
		for (Iterator<Entry<Integer, Integer>> it = ordered.iterator(); it.hasNext();) {
			result.add( it.next().getKey() );
        }		
		return result;
	}
	
	public TitleFinder(String titleFile) throws IOException {
		this.basePath = Paths.get(emptyStr);
		this.basePathStr = this.basePath.toAbsolutePath().toString();
				
		this.wordInTitleMap = new HashMap<String, Object>();
		this.titles = new ArrayList<String>();
		
		this.loadStopWords();
		this.parseTitleFile(titleFile);		
		
	}
	
	@SuppressWarnings("unchecked")
	private Collection<Integer> searchWordInTitles(String word) {
		if (stopWords.contains(word)) {
			return null;
		}
		return (Collection<Integer>) this.wordInTitleMap.get(word);
	}
	
	private String askForSearch() throws IOException {
		print("Type a word to search for in available titles: ");
		return normalizeText(reader.readLine());
	}
	
	private String normalizeText(String text) {
		
		if (replacement == null) {
			replacement = new String[toReplace.length];
			for (int i=0; i < toReplace.length; i++) {
				replacement[i] = emptyStr;
			}
		}
		
		text = StringUtils.stripAccents(text.trim()).toLowerCase();
		return StringUtils.replaceEach(text, toReplace, replacement);
	}
	
}
