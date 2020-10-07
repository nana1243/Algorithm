package graph;


import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class p1 {

	public static void main(String[] args) {

		int n = 6;
		int[][] edge = { { 3, 6 }, { 4, 3 }, { 3, 2 }, { 1, 3 }, { 1, 2 }, { 2, 4 }, { 5, 2 } };
		int ans = solution(n, edge);
		

	}

	static int solution(int n, int[][] edge) {

		boolean[] visited = new boolean[n+1];
		Queue<Integer> queue = new LinkedList<>();
		HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();

		LinkedList<Integer>[] adj = new LinkedList[n+1];
		
		// graph 만들기
		for(int i=1;i<n+1;i++) {
			adj[i] = new LinkedList<Integer>();
			map.put(i, 0);
		}

		for (int[] elm : edge) {
			adj[elm[0]].add(elm[1]);
			adj[elm[1]].add(elm[0]);

		}
		
		//bfs실행
		
		queue.add(1);
		visited[1] = true;
		map.put(1, map.get(1) + 1);
		System.out.println(map);
		
		while(!queue.isEmpty()) {
			int out = queue.remove();
			
			for(int elm : adj[out]) {
				if(visited[elm]==false) {
					visited[elm]=true;
					queue.add(elm);
					map.put(elm, map.get(out) + 1);
				}
			}
			
			
		}
		System.out.println(map);
		int max =Collections.max(map.values());
		int ans=0;
		for(int i=1;i<=map.size();i++) {
			if(map.get(i)==max) {
				ans++;
			}
		}
		
		return ans;
		

	}
	

}
