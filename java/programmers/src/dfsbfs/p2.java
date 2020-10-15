package dfsbfs;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class p2 {
	
	// java is kuk hyum..
	public static void bfs(HashSet<Integer> graph,int start) {
		
		Queue<Integer>que = new LinkedList<>();
		que.add(start);
		
		while(!que.isEmpty()) {
			
			int out = que.poll();
			
			for(HashSet<Integer> elm : graph[out]) {
				System.out.println("check yo gi su bu tu");
			}
			
		}
		
		
	}
	
	

	public static void main(String[] args) {
		
		// ha....hagisiro..real...its real
		
		
		
		int n = 3;
		int[][] computers = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
		
		Set<Integer>[] graph =  new HashSet[n];
		int[] visit = new int[n];
		
		// makegraph
		
		for(int i=0;i<n;i++) {
			graph[i] = new HashSet<>();
			for(int j=0;j<n;j++) {
				if(computers[i][j]==1 && i!=j) {
					graph[i].add(j);
					
				}
			}
			
		}
		
		
	
		
	}
	
}