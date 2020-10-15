package greedy;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class p4 {

	public static void main(String[] args) {
		
		int[] people = {70, 80, 50,40};
		
		int limit = 100;
		int ans=0;
		
		Arrays.sort(people);
	
		
		int i=0;
		int heavy = people.length-1;
		
		while (i<heavy) {
			if( people[i] + people[heavy] <=limit) {
				i++;
				ans++;
			}
			heavy--;
		}
		
		System.out.println();
	
	}

}
