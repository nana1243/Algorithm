package test;

import java.util.Comparator;
import java.util.PriorityQueue;

public class PriorityTest {

	public static void main(String[] args) {
		
		
		int[] test1 = {1,2,3,4,9,11,12,15,200,2};
		
		
		
		
		
		 PriorityQueue<Integer> max = new PriorityQueue<Integer>(new Comparator<Integer>() {
			public int compare(Integer o1, Integer o2) {

				if (o1 < o2) {
					return 1;
				}
				return -1;
			};
		});
		 
		 
		 for(int elm : test1) {
			 max.add(elm);
		 }
		 
		 // peek
		 
		 int peek = max.peek();
		 System.out.println(peek);
		
		 
		 int poll = max.poll();
		 System.out.println(peek);


	}

}
