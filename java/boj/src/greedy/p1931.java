package greedy;


import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;



public class p1931 {
	
	
	public static int solution(int[][] arr) {
		int start =  arr[0][0];
		int end = arr[0][1];
		int cnt=1;
		
		for(int i=1;i<arr.length;i++) {
			
			if( end<=arr[i][0]) {
				cnt+=1;
				start = arr[i][0];
				end = arr[i][1];
				
			}
		}
		
		return cnt;
	}
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] arr= new int[n][2];
		for(int i=0;i<arr.length;i++) {
			arr[i][0] = sc.nextInt();
			arr[i][1] = sc.nextInt();
		
		}
		
		Arrays.sort(arr, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
	
				return o1[0]-o2[0];
			}
		});
		
	
		int ans1= solution(arr);
		Arrays.sort(arr, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
	
				return o1[1]-o2[1];
			}
		});
		
		int ans2= solution(arr);
		
		int ans = Math.max(ans1, ans2);
		System.out.println(ans);
	}

}
