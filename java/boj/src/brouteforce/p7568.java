package brouteforce;

import java.util.Scanner;

public class p7568 {
	
	
	 static int[] compare(int[][] arr) {
		int[] ans = new int[arr.length];
		
		
		for(int i=0;i<arr.length;i++) {
			int weight = arr[i][0];
			int height = arr[i][1];
			int rank =1;
			
			for(int j=0;j<arr.length;j++) {
				if(weight<arr[j][0] && height<arr[j][1]) {
					rank+=1;
				}
			}
		 ans[i] = rank;
		}
		
		return ans;
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int[][] arr = new int[n][2];
		
		for(int i=0;i<n;i++) {
			arr[i][0] = sc.nextInt();
			arr[i][1] = sc.nextInt();
		}
		
		
		int[] ans = compare(arr);
		StringBuilder sb = new StringBuilder();
		for(int elm : ans) {
			sb.append(elm+" ");
		}
		System.out.println(sb.toString().trim());
		
	}

}
