package graph;

import java.util.HashSet;
import java.util.Set;

public class p2 {

	public static void main(String[] args) {
		int n = 5;
		int[][] results = { { 4, 3 }, { 4, 2 }, { 3, 2 }, { 1, 2 }, { 2, 5 } };

		Graph g = new Graph(n, results);
		g.make_graph();

		g.upgrade_graph();

		int ans = g.make_answer();
		System.out.println(ans);

	}

}

class Graph {

	int n;
	int[][] results;
	Set<Integer>[] win;
	Set<Integer>[] lose;

	public Graph(int n, int[][] results) {
		this.n = n;
		this.results = results;

		win = new HashSet[n + 1];
		lose = new HashSet[n + 1];

		for (int i = 1; i < n + 1; i++) {
			win[i] = new HashSet<>();
			lose[i] = new HashSet<>();

		}

	}

	public void make_graph() {
		for (int[] elm : results) {
			win[elm[0]].add(elm[1]);
			lose[elm[1]].add(elm[0]);
		}
	}

	public void upgrade_graph() {

		for (int i = 1; i < n + 1; i++) {
			for (int loser : win[i]) {
				lose[loser].addAll(lose[i]);

			}
			for (int winner : lose[i]) {
				win[winner].addAll(win[i]);
			}

		}

	}

	public int make_answer() {
		int res = 0;
		for (int i = 1; i < n + 1; i++) {
			if (win[i].size() + lose[i].size() == n - 1) {
				res++;
			}
		}
		return res;
	}

}