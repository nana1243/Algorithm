package stackandque;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class p2 {
	
	
	static int complete(int progress, int speed) {
		
		int res = (int) Math.ceil(((float)(100-progress)/speed));
		return res;
	}
	
	
    static public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        Queue<Integer> result= new LinkedList<>();
      
       
        for (int i=0;i<progresses.length;i++) {
        	int day = complete(progresses[i], speeds[i]);
        	result.add(day);
        }
       
        while (!result.isEmpty()) {
        	
        	
        	
        	int cnt=1;
        	int out = result.remove();
        	System.out.println(result);
        
        	while(!result.isEmpty() && out>=result.peek()) {
        		result.remove();
        		cnt+=1;
        	}
        	
        	arr.add(cnt);
        	cnt=1;
        }
        int[] answer = new int[arr.size()];
        
        for(int i=0; i<answer.length;i++) {
        	answer[i] = arr.get(i);
        }
    
        return answer;
    }
    
    
	public static void main(String[] args) {
		int[] progresses = {95, 90, 99, 99, 80, 99};
		int[] speeds = {1, 1, 1, 1, 1, 1};
		
		int[] ans = solution(progresses, speeds);
		System.out.println(Arrays.toString(ans));
		
	}
}
