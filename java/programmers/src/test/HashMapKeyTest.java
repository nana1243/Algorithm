package test;

import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class HashMapKeyTest {

	public static void main(String[] args) {
	
		
		HashMap<String, Integer> map1 = new HashMap<String, Integer>();
		
		
		map1.put("hennie",1);
		map1.put("zennie",10);
		map1.put("punnie",2);
		map1.put("qunnie",3);
		System.out.println(map1);
		
		
		// map의 key값들 정렬
		
		
		
		
		// 오름차순
		List<Map.Entry<String, Integer>> list = new LinkedList<>(map1.entrySet());		

		Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {

			@Override
			public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
				if(o1.getValue()>o2.getValue()) {
					return 1;
				}
				return -1;
			}
			
			
		});
		
		System.out.println(list);
		
		// 내림차순
		
		

		Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {

			@Override
			public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
				if(o1.getValue()>o2.getValue()) {
					return -1;
				}
				return 1;
			}
			
			
		});
		
		// lambda 식 표현
		
		list.forEach((Map.Entry<String, Integer> elm) -> System.out.println(elm.getKey()));
		
		
		

	}

}
