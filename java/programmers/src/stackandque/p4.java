package stackandque;

import java.util.Deque;
import java.util.LinkedList;

public class p4 {
	static public int solution(int[] priorities, int location) {
		
		Deque<int[]> queue = new LinkedList<>();
	
		for(int i=0;i<priorities.length;i++) {
			int[] tmp = {i,priorities[i]};
			queue.add(tmp);
			
		}
	
	
		int ans[][] = new int[priorities.length][2];
		
		
		int cnt=0;
		while(!queue.isEmpty()) {
			
			int[] out = queue.remove();
			
			for(int[] elm : queue ) {
				if(out[1]<elm[1]) {
					queue.add(out);
					break;
				}
			}
			
		if(queue.peekLast()==out) {
			continue;
		}else {
			ans[cnt] = out;
			if(out[0]==location) {
				return cnt+1;
			}
			cnt+=1;
		}

		}
		return cnt+1;

		
	}

	public static void main(String[] args) {

		int[] priorities = { 1, 1, 9, 1, 1, 1 };
		int location = 0;
		int ans = solution(priorities, location);

		System.out.println(ans);

	}

}
