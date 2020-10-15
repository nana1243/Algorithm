package heap;

import java.util.Collection;
import java.util.Comparator;
import java.util.PriorityQueue;

public class p2 {

	static int[] calculateTime(int curtime, int waitingtime, int worktime) {

		int anstime = worktime + (curtime - waitingtime);
		curtime += worktime;

		return new int[] { anstime, curtime };
	}
	


	public static void main(String[] args) {

		int[][] jobs = { { 0, 3 }, { 1, 9 }, { 2, 6 } };

		int time = 0;
		

		PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[1] < o2[1]) {
					return -1;
				}
				return 1;

			}
		});
		
		for(int[] elm : jobs) {
			pq.add(elm);
		}
		
		
		while(!pq.isEmpty()) {
			PriorityQueue<int[]> ing = new PriorityQueue<>(new Comparator<int[]>() {
				@Override
				public int compare(int[] o1, int[] o2) {
					if (o1[1] < o2[1]) {
						return -1;
					}
					return -1;

				}
			});
		}

	}
}
