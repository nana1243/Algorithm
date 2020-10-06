package backtracking;

import java.util.Scanner;

public class p15650 {
	static int n;
	static int m;
	static StringBuilder sb;
	
    public static void combination(int cur, String str,int start) {
        if (cur == m) {
        	System.out.println(sb);
            sb.append(str.trim() + "\n");
        } else {
            ++cur;
            for (int i = start ; i <= n; i++) {
                    combination(cur, str + " " + i, i+1);
            }
        }
        }
	

	public static void main(String[] args) {
	
		
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		
		sb = new StringBuilder();
		combination(0, "", 1);
		System.out.println(sb);
		

	}

}
