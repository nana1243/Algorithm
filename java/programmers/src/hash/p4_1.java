package hash;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class p4_1 {

	public static void main(String[] args) {
		String[] genres = { "classic", "pop", "classic", "classic", "pop" };
		int[] plays = { 500, 600, 150, 800, 2500 };

		HashMap<String, Object> genresMap = new HashMap<String, Object>(); // <장르, 곡 정보>
		HashMap<String, Integer> playMap = new HashMap<String, Integer>(); // <장르, 총 장르 재생수>
		ArrayList<Integer> resultAL = new ArrayList<Integer>();

		// <장르 : total곡>

		for (int i = 0; i < genres.length; i++) {
			playMap.put(genres[i], +plays[i]);
		}

		System.out.println(playMap);

		List<Map.Entry<String, Integer>> list = new LinkedList<>(playMap.entrySet());

		Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {

			@Override
			public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
				int comparision = (o1.getValue() - o2.getValue()) * -1;
				return comparision == 0 ? o1.getKey().compareTo(o2.getKey()) : comparision;
			}

		});
		// <장르 : {}>

		for (int i = 0; i < genres.length; i++) {

			String key = genres[i];
			int index = i;
			int value = plays[i];
			HashMap<Integer, Integer> info;

			if (genresMap.containsKey(key)) {

				// 해당키의 hashmap을 불러온다

				info = (HashMap<Integer, Integer>) genresMap.get(key);

				genresMap.put(key, info);
				info.put(index, value);
			} else {

				info = new HashMap<Integer, Integer>();
				info.put(index, value);
				genresMap.put(key, info);

			}

		}

	}

}
