package dfsbfs;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;



public class p2 {

	static int n;
	static int[][] computers;
	static Set<Integer>[] graph;
	static boolean[] visit;

	public static void bfs(int start) {

		Queue<Integer> que = new LinkedList<>();

		que.add(start);

		while (!que.isEmpty()) {

			int out = que.poll();
			for (Integer elm : graph[out]) {
				if (visit[elm] == false) {
					visit[elm] = true;
					que.add(elm);

				}
			}

		}

	}

	public static void main(String[] args) {
		 n = 3;
		computers = new int[][] {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};

		graph = new HashSet[n+1];

		visit = new boolean[n+1];

		for (int i = 0; i < computers.length; i++) {
			graph[i] = new HashSet<>();

			for (int j = 0; j < computers[i].length; j++) {
				if (j != i && computers[i][j] == 1) {
					graph[i].add(j);
				}
			}

		}

		int ans = 0;
		for (int i = 0; i < n; i++) {
			if (visit[i] == false) {
				bfs(i);
				ans++;
			}
		}

		System.out.println(ans);

	}

}
