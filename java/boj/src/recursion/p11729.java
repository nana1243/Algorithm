package recursion;

import java.util.Scanner;

public class p11729 {
	
	
	static int total;
	static StringBuilder sb ;

	
	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		int n = sc.nextInt();
		sb = new StringBuilder();
		
		hanoi(n, 1, 2, 3);
		System.out.println(total);
		System.out.println(sb);
		
		
		
		
	}
	
	 static void hanoi(int n, int start, int via, int end) {
		 total++;
		if(n==1) {
			sb.append(start +" "+ end + "\n");
		}else {
			hanoi(n-1,start,end,via);
			sb.append(start + " " +via+ "\n");
			hanoi(n-1, via, start, end);
				
		}
	
		
	}

}
