package greedy;

import java.util.Scanner;



public class p11047 {

	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		int ans =0;
		
		int[] coins = new int[n];
		for(int i=0;i<n;i++) {
			coins[i] = sc.nextInt();
		}
				
		for (int j =n-1;j>=0;j--) {
			
			int tmp = m/coins[j];
			m -= tmp*coins[j];
			ans+=tmp;
		}
		
		System.out.println(ans);
	}

}
