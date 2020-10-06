package test;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class test {

	public static void main(String[] args) {
		
		String[] test1 = {"20+30","30+40","40+30"};
		
//		for(String elm : test1) {
//			System.out.println(elm);
//			
//			String[] test1_1= elm.split("\\+");
//			
//			System.out.println(Arrays.toString(test1_1));
//		}
//		
		LinkedList<Integer> test2 = new LinkedList<>();
		test2.add(1);
		test2.add(2);
		test2.add(3);
		
		System.out.println(test2.get(0));
		
		Queue<Integer> test3 = new LinkedList<>();
		test3.add(1);
		test3.add(2);
		test3.add(3);
		
		System.out.println(test3);
		System.out.println(test3.peek());




	}
	
	
	

}
