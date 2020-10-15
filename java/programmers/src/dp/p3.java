package dp;


// % 1000000007 붙여주냐에 따라 효율성 넘어가고 안넘어가고

public class p3 {

	static boolean search(int i, int j, int[][] puddles) {

		for (int[] elm : puddles) {
			if (i == elm[0]-1 && j == elm[1]-1) {
				return true;
			}
		}

		return false;
	}

	static int[][] shortPath(int n, int m, int[][] puddles) {
		int[][] ans = new int[n][m];
		ans[0][0] = 1;

		for (int i = 0; i < n; i++) {// y
			for (int j = 0; j < m; j++) { // x

				if (search(i, j, puddles) == true) {
					ans[i][j] = 0;
					continue;
				}
				if (j > 0) {
					ans[i][j] += ans[i][j - 1]% 1000000007;
				}
				if (i > 0) {
					ans[i][j] += ans[i - 1][j]% 1000000007;
				}

			}
		}

		return ans;

	}

	public static void main(String[] args) {

		int m = 4;
		int n = 3;
		int[][] puddles = { { 2, 2 } };

		int[][] path = shortPath(n, m, puddles);
		int answer = path[n - 1][m - 1]% 1000000007;
		
		
		System.out.println(answer);
	}

}
