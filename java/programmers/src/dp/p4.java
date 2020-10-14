package dp;



// ArrayList 와 array 의 차이에 따라 시간 효율성 통과 유/무


public class p4 {
	
	
	
	

	public static void main(String[] args) {
		int[] money = {1, 2, 3, 1};
		int n = money.length;
		
		int[] arr0 = new int[n-1];
		int[] arr1 = new int[n];
		
		arr0[0] = money[0];
		arr0[1] = money[0];

		arr1[0] = 0;
		arr1[1] = money[1];

		
		for(int i=2; i<n-1 ;i++) {
			arr0[i] = Math.max( arr0[i-2]+ money[i], arr0[i-1] );
		}
		
		for(int i=2; i<n ;i++) {
			arr1[i] = Math.max( arr1[i-2]+ money[i], arr1[i-1] );
		}
		

	}


}
