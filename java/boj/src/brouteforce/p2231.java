package brouteforce;

import java.util.Scanner;

public class p2231 {

	public static int split(int n) {
		int ans =0;
		while(n>0) {
			ans += n%10;
			n /=10;
		}
		return ans;
	}
	
	public static int constructor(int n) {
		int ans = n;
		for (int i=0;i<n+1;i++) {
			if ( i+ split(i)==n) {
				ans = Math.min(ans, i);
			}
		}
		if(ans==n) {return 0;}
		
		return ans;
	}
	
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int ans = constructor(n);
		System.out.println(ans);
		
	}

}
