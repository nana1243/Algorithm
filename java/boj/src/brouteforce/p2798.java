package brouteforce;

import java.util.Scanner;

public class p2798 {
	
	
	public static void main(String[] args) {
		
		
		Scanner sc =  new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int ans =0;
		
		int[] arr = new int[n];
		for(int i=0; i<n;i++) {
			arr[i] = sc.nextInt();
		}
		
		// 3���� �����Ѵ� => limit�� �������� ���� �����Ѵ�
		
		for(int i=0;i<n;i++) {
			for(int j =i+1; j<n;j++) {
				for(int u= j+1;u<n;u++) {
					int tmp = arr[i]+arr[j] + arr[u];
					if(tmp<=m) {
						ans = Math.max(ans, tmp);
					}
				}
			}
		}

		System.out.println(ans);
	}
	

}
