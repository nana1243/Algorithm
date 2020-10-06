package backtracking;

import java.util.Scanner;

public class p15652 {
	static int n;
	static int m;
	static StringBuilder sb;

	public static void dfs(int start, String str, int cur) {

		if (cur == m) {
			sb.append(str.trim()+"\n");
		} else {
			cur++;
			for(int i=start;i<=n;i++) {
				dfs(i,str+" " +i, cur);
			}

		}

	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();

		sb = new StringBuilder();
		dfs(1,"",0);
		System.out.println(sb);

	}

}
