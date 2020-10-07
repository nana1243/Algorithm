package test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class hashset {

	public static void main(String[] args) {
		Set<Integer>[] win ;
		Set<Integer>[] lose ;
		int n =6;
		
		win = new HashSet[n+1] ;
		lose = new HashSet[n+1];
		
		
		
		for(int i=1;i<n+1;i++) {
			win[i] = new HashSet<>();
			win[i].add(1);
		}
		System.out.println(Arrays.toString(win));
		
		
		
		
	}

}
