package test;

import java.util.Collections;
import java.util.TreeMap;

public class TreeMapKeyTest {

	public static void main(String[] args) {

		// key값을 정렬하지 않아도 알아서 정렬
		
		
		//1. string:int treemap 정렬
		
		TreeMap<String, Integer> map1 = new TreeMap<>();

		map1.put("test1", 2);
		map1.put("test2", 4);
		map1.put("test3", 1);
		map1.put("test4", 7);
		System.out.println(map1);
		
		//2. int:int treemap 정렬


		TreeMap<Integer,Integer> map2 = new TreeMap<>();

		map2.put(1, 2);
		map2.put(4, 4);
		map2.put(2, 1);
		map2.put(3, 7);
		System.out.println(map2);
		
		
		
		// key값을 내림차순으로 하려면?
		

		TreeMap<String, Integer> map3 = new TreeMap<>(Collections.reverseOrder());
		
		map3.put("test1", 2);
		map3.put("test2", 4);
		map3.put("test3", 1);
		map3.put("test4", 7);
		System.out.println(map3);

	
		

	}

}
