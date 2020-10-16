package test;

import java.util.Collections;
import java.util.TreeMap;

public class TreeMapKeyTest {

	public static void main(String[] args) {

		// key���� �������� �ʾƵ� �˾Ƽ� ����
		
		
		//1. string:int treemap ����
		
		TreeMap<String, Integer> map1 = new TreeMap<>();

		map1.put("test1", 2);
		map1.put("test2", 4);
		map1.put("test3", 1);
		map1.put("test4", 7);
		System.out.println(map1);
		
		//2. int:int treemap ����


		TreeMap<Integer,Integer> map2 = new TreeMap<>();

		map2.put(1, 2);
		map2.put(4, 4);
		map2.put(2, 1);
		map2.put(3, 7);
		System.out.println(map2);
		
		
		
		// key���� ������������ �Ϸ���?
		

		TreeMap<String, Integer> map3 = new TreeMap<>(Collections.reverseOrder());
		
		map3.put("test1", 2);
		map3.put("test2", 4);
		map3.put("test3", 1);
		map3.put("test4", 7);
		System.out.println(map3);

	
		

	}

}
