package brouteforce;

import java.util.HashSet;

public class p2 {
	
	 static void permutation(String prefix, String str, HashSet<Integer> set) {
	        int n = str.length();
	        //if (n == 0) System.out.println(prefix);
	        if(!prefix.equals("")) set.add(Integer.valueOf(prefix));
	        for (int i = 0; i < n; i++)
	          permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n), set);

	    }

	static boolean isPrime(int m) {
		if (m <= 2) {
			return false;
		}
		int n = (int) Math.sqrt(m);

		for (int i = 3; i < n + 1; i++) {
			if (m % i == 0) {
				return false;
			}
		}
		return true;
	}
	

	public static void main(String[] args) {
		 String numbers = "17";
		 HashSet<Integer> set = new HashSet<>();
	     permutation("", numbers, set);
		
		
		

	}

}
