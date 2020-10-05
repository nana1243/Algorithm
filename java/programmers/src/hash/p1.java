package hash;

import java.util.HashMap;

public class p1 {
	
	
	 static  String solution(String[] participant, String[] completion) {
		 
		 HashMap<String, Integer> map = new HashMap<String, Integer>();
			
			for(String person : completion) {
				map.put(person, map.getOrDefault(person, 0)+1);
			}
		
			
			for(String person : participant) {
				map.put(person, map.getOrDefault(person,0)-1);
			
	            if (map.get(person) <0)
	                return person;
				
			}
						
			return "";
	 }
	
	
	public static void main(String[] args) {
		
		String[] participant = {"marina", "josipa", "nikola", "vinko", "filipa"};
		String[] completion ={ "josipa", "filipa", "marina", "nikola"};
		
		String ans = solution(participant, completion);
		System.out.println(ans);
			
		}
		
	
}
