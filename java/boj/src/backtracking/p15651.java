package backtracking;

import java.util.Scanner;

public class p15651 {

	    static int[] num;
	    static int n;
	    static int m;
	    static StringBuilder sb = new StringBuilder();

	    public static void main(String[] args) {
	        Scanner sc = new Scanner(System.in);
	        n = sc.nextInt();
	        m = sc.nextInt();
	        num = new int[m + 1];
	        dfs(1);
	        System.out.println(sb);
	    }

	    static void dfs(int current) {
	        if (current > m) {
	            for (int i = 1; i <= m; i++) {
	                sb.append(num[i]).append(" ");
	            }
	            sb.append("\n");
	            return;
	        }
	        for (int i = 1; i <= n; i++) {
	            num[current] = i;
	            dfs(current + 1);
	        }
	    }

}
