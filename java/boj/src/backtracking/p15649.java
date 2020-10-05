package backtracking;

import java.util.LinkedList;
import java.util.Scanner;

public class p15649 {
	
	static LinkedList<Integer> list;
	static boolean[] visited;
	
	
	public static void permutation(int n,int m) {
		if(m==0) {
			for(int elm: list) {
				System.out.print(elm+" ");
			}
			System.out.println();
		}else {
			for(int i=1;i<n+1;i++) {
				if(!visited[i]) {
					visited[i]= true;
					list.add(i);
					permutation(n,m-1);
					list.removeLast();
					visited[i] = false;
				}
			}
			
		}
		
		
	}

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		list = new LinkedList<Integer>();
		visited = new boolean[n+1];
		permutation(n, m);
		

	}

}
