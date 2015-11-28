package titlefinder;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.BeforeClass;
import org.junit.Test;

import br.com.luizcapu.titlefinder.TitleFinder;

public class TitleFinderTest {
	
	private static TitleFinder finder;
	private static final String resourcesPath = "/src/main/resources/";
	private static final String defaultTitleFileName = "example.txt";
	
	@BeforeClass
	public static void setUp() throws IOException{
		String payloadFile = Paths.get("").toAbsolutePath().toString() + resourcesPath + defaultTitleFileName;
		finder = new TitleFinder(payloadFile);
	}
	
	@Test
	public void testFrequencyOrder() throws Exception {
		List<Integer> expected = new ArrayList<Integer>(Arrays.asList(2, 0, 1));
		checkResults(expected, finder.searchWordInTitles("demora"));
	}

	@Test
	public void testNotFound() throws Exception {
		checkResults(null, finder.searchWordInTitles("thisstringshouldnotbefound"));
	}

	@Test
	public void testNormalization() throws Exception {
		List<Integer> expected = new ArrayList<Integer>(Arrays.asList(2, 0, 1));
		checkResults(expected, finder.searchWordInTitles("dÊMórÁ"));
	}
	
	@Test
	public void testOneResult() throws Exception {
		List<Integer> expected = new ArrayList<Integer>(Arrays.asList(3));
		checkResults(expected, finder.searchWordInTitles("estatua"));
	}
	
	static void print(String msg) {
		System.out.println("========================================================");
		System.out.println(msg);
		System.out.println("========================================================");
	}
	
	private void checkResults(List<Integer> expected, List<Integer> got) {
		StackTraceElement[] stacktrace = Thread.currentThread().getStackTrace();
		StackTraceElement e = stacktrace[2];//maybe this number needs to be corrected
		String callerName = " - (" + e.getMethodName() + ")";
		
		if (expected == null) {
			assertBool(got == null, "\"Got\" should be null" + callerName);					
		} else {
			assertBool(expected.size()==got.size(), "\"Expected\" and \"got\" items size" + callerName);		
			for (int i=0; i < expected.size(); i++) {
				assertBool(expected.get(i)==got.get(i), "Element "+i+" equals in both \"expected\" and \"got\"" + callerName);
			}			
		}
	}
	
	private void assertBool(boolean b, String string) {
		if (!b) {
			String message = "Error in assertion: " + string;
			print(message);
			throw new RuntimeException(message);
		} else {
			print(string);
		}
	}
	
}
