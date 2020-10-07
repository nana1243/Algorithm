package backtracking;


import java.util.Scanner;

public class p9663 {
	static int n, ans;
	static boolean[] a, b, c;

	static void dfs(int i) {

		if (i == n) {
			ans += 1;

		}
		for (int j = 0; j < n; j++) {
			if ((a[j] == false && b[i + j] == false && c[i - j + n - 1] == false)) {
				a[j] = b[i + j] = c[i - j + n - 1] = true;
				dfs(i + 1);
				a[j] = b[i + j] = c[i - j + n - 1] = false;

			}
		}

	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		ans = 0;

		a = new boolean[n];
		b = new boolean[2 * n - 1];
		c = new boolean[2 * n - 1];

		dfs(0);
		System.out.println(ans);

	}

}
