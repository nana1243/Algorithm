package dfsbfs;


import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

public class p3 {
	
	static private String begin;
	static private String target;
	static private String[] words;
	static private boolean[] visit;
	static private HashSet<Integer> layer;
	static private HashMap<String,List<String>>graph;
	
	
	
	public static int check(String str1, String str2) {
		
		int ans=0;
		for(int i=0;i<str1.length();i++) {
			if(str1.charAt(i)!=str2.charAt(i)) {
				ans++;
			}
			
		}
		return ans;
	}
	
	public static void makeGraph() {
		
		graph = new HashMap<String, List<String>>();
		
		for(int i=0;i<words.length;i++) {
			if(graph.containsKey(words[i])) {
				
			}
			else {
				
				List<Integer> tmp = new LinkedList<>();
				graph.get(words[i]))
			}
			
		}
		
		
	}
	
	public static void bfs(String begin) {
		
		
		
	}
	
	

	public static void main(String[] args) {
		
	target = "cog";
	
	words = new String[] {"hot", "dot", "dog", "lot", "log", "cog"};
	
	
		
		

	}

}
