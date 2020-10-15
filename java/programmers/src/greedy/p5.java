package greedy;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Stack;

public class p5 {
	
// 덜풀엇당 여기서부터

	public static void main(String[] args) {
		
		int n =4;
		int[][] costs = {{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}};
	
		
		Arrays.sort(costs, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				
				return o2[2] - o1[2];
			}
		});
		
		for(int[] elm : costs) {
			System.out.println(Arrays.toString(elm));
		}
		
		  LinkedList<Integer> stack = new LinkedList<Integer>();
		  
		  
	}

}



class Hamilton{
	
	int n;
	int[] p;
	int[][] costs;
	
	
	public Hamilton(int n, int[][] costs) {
		this.n = n;
		this.costs = costs;
	}
	
	public void makePlist(){
		
		for(int i=0;i<n;i++) {
			p[i] = i;
		}
	}
	
	
	
	public int find(int u) {
		if(p[u]!=u) {
			u = find(p[u]);
		}
			
	 return u;
	}
	
	public void union(int u, int v) {
		
		int root1 = find(u);
		int root2 = find(v);
		
		if(root1!=root2) {
			p[root2] =root1;
		}
		
	}
	public void connect() {
		
	
		
	}
	
	
	
}