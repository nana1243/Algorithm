package dp;

import java.util.Arrays;

import java.lang.Math;

public class p2 {

	public static int dp(int[][] dp) {

		int ans = 0;

		for (int i = 1; i < dp.length; i++) {
			for (int j = 0; j <=dp[i].length-1; j++) {
				if (j == 0) {
					dp[i][j] += dp[i - 1][j];
				
				} else if (j == dp[i].length - 1) {
					
					dp[i][j] += dp[i - 1][j-1];
				} else {
					dp[i][j] += Math.max(dp[i - 1][j - 1], dp[i - 1][j]);
				}
			
				ans = Math.max(ans, dp[i][j]);
			}
			System.out.println(Arrays.toString(dp[i]));

		}
		
		return ans;

	}

	public static void main(String[] args) {
		int[][] triangle = { { 7 }, { 3, 8 }, { 8, 1, 0 }, { 2, 7, 4, 4 }, { 4, 5, 2, 6, 5 } };
		
		
		int ans = dp(triangle);
		System.out.println(ans);

	}

}
