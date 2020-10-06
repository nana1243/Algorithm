package stackandque;

import java.util.Arrays;
import java.util.Stack;

public class p1 {
	
	
	// 주식가격
    static int[] solution(int[] prices) {
    	
    	int[] answer = new int[prices.length];
    	Stack<Integer> stack = new Stack<Integer>();
    	
    	
    	for(int i=0;i<prices.length;i++) {
    		answer[i]= prices.length-1-i;
    	}
    	
    	for (int i=0;i<prices.length;i++) {
    		int price = prices[i];
    		
    		while ( stack.size()!=0 && price<prices[ stack.get(stack.size()-1) ] ) {
    			int last = stack.pop();
    			answer[last] = i - last;
    			
    		}
    		stack.add(i);
    		
    	}
    	
    	
        return answer;
		
    	
	  }
	public static void main(String[] args) {
		
		
		int[] prices = {1, 2, 3, 2, 3};
		int[] answer = solution(prices);
		System.out.println(Arrays.toString(answer));
	}

}
