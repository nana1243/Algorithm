package recursion;

import java.util.Scanner;

public class p10872 {
	
	public static int factorial(int number) {
		
		if(number ==1) {
			return 1;
		}
		
		return number*factorial(number-1);
	}
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int number = sc.nextInt();
		
		int ans= factorial(number);
		
		System.out.println(ans);

	}

}
