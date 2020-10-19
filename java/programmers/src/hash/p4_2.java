package hash;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class p4_2 {

	public static void main(String[] args) {
		String[] genres = { "classic", "pop", "classic", "classic", "pop" };
		int[] plays = { 500, 600, 150, 800, 2500 };

		HashMap<String, Object> genresMap = new HashMap<String, Object>(); // <장르, 곡 정보>
		HashMap<String, Integer> playMap = new HashMap<String, Integer>(); // <장르, 총 장르 재생수>
		ArrayList<Integer> resultAL = new ArrayList<Integer>();

		for (int i = 0; i < genres.length; i++) {
			playMap.put(genres[i], +plays[i]);
		}

		System.out.println(playMap);

		List<Map.Entry<String, Integer>> list = new LinkedList<>(playMap.entrySet());

		System.out.println(list);

		// 내림차순
		Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
			@Override
			public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
				if (o1.getValue() > o2.getValue()) {
					return -1;
				}
				return 1;
			}

		});

		int idx = 0;
		for (Map.Entry<String, Integer> elm : list) {

			genresMap.put(elm.getKey(), new HashMap<Integer, Integer>());

		}

		for (int i = 0; i < genres.length; i++) {
			String key = genres[i];

			HashMap<Integer, Integer> info = (HashMap<Integer, Integer>) genresMap.get(key);
			info.put(i, plays[i]);

		}

		for (Map.Entry<String, Integer> elm : list) {
			String key = elm.getKey();

			HashMap<Integer, Integer> info = (HashMap<Integer, Integer>) genresMap.get(key);
			List<Map.Entry<Integer, Integer>> info_list = new LinkedList<>(info.entrySet());

			Collections.sort(info_list, new Comparator<Map.Entry<Integer, Integer>>() {
				@Override
				public int compare(Entry<Integer, Integer> o1, Entry<Integer, Integer> o2) {

					if (o1.getValue() > o2.getValue()) {
						return 1;
					}
					return -1;

				};
			});
			
			
			//

		}
		
		
		
	}

}