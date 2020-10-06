package greedy;

import java.util.Arrays;
import java.util.Scanner;

public class p11399 {

	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		
		int n = sc.nextInt();
		int ans =0;
		
		
		int[] arr = new int[n];
		for (int i=0;i<n;i++) {
			arr[i]= sc.nextInt();
		}
		
		Arrays.sort(arr);
		
		for(int i=0;i<n;i++) {
			
			for(int j =0;j<i+1;j++) {
				ans+=arr[j];
			}
		}
		
		System.out.println(ans);
		

	}

}
