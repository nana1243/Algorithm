package hash;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;

public class p4 {
	
	
	 static void solution(String[] genres, int[] plays) {
		 
		 //1 . total을 구한다
		 //2. 장르별로 sort한다
		 //3. 해당 장르중에서도 
		 
		 HashMap<String, Integer> hash_genres = new HashMap<String, Integer>();
		 for(int i=0;i<genres.length;i++) {
			 hash_genres.put(genres[i], +plays[i]);
		 }
		 
		 
		 System.out.println(hash_genres);
		 ArrayList<String> keySetList = new ArrayList<String>(hash_genres.keySet());
		 System.out.println(keySetList);
		 Collections.sort(keySetList, new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				return hash_genres.get(o1).compareTo(hash_genres.get(o2));
			}
		});
		 
		System.out.println(keySetList);
		 
	 }

	public static void main(String[] args) {
		
		String[] genres = {"classic", "pop", "classic", "classic", "pop"};
		int[] plays = 	{500, 600, 150, 800, 2500};
		
		solution(genres, plays);
		
	
	}

}
