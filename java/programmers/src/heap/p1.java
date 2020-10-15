package heap;

import java.util.PriorityQueue;

public class p1 {
	
	
	static int score(PriorityQueue<Integer> pq) {
		
		int res1 = pq.poll();
		int res2 = pq.poll();
		int res =  res1 + (res2 *2);
		return res;
	}
	
	public static void main(String[] args) {
	
		int[] scoville = {1, 2, 3, 9, 10, 12};
		int K = 7;
		int cnt = 0;
		
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		
		for(int elm : scoville) {
			pq.add(elm);
		}
		
		
		try {
			
			while (pq.peek()<K) {
				int out = score(pq);
				pq.add(out);
				cnt++;
			}
			System.out.println(cnt);
		}
			
		catch (Exception e) {
		
		System.out.println(-1);
	}
		
		
	}
}
