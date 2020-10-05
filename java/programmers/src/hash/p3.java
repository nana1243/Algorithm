package hash;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class p3 {
	
	// 서로 다른 옷의 조합의 수를
	
	  static public int Solution(String[][] clothes) {
		  
		 
		 HashMap<String, Integer> map = new HashMap<String, Integer>();
		 
		 for(String[] elm : clothes) {
			 map.put(elm[1], map.getOrDefault(elm[1],1)+1);
		 }
		 
		 
		int ans =1;
		
		for(int elm : map.values()) {
			ans*=elm;
		}

		return ans-1;
		 
	 }

	public static void main(String[] args) {
		
		String[][] clothes= { 
				{"yellow_hat", "headgear"}, 
				{"blue_sunglasses", "eyewear"},
				{"green_turban", "headgear"}
		};
		
		int ans = Solution(clothes);
		System.out.println(ans);

	}

}
