package greedy;


import java.util.Arrays;
import java.util.Scanner;

public class p1541 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		
		String[] s = sc.nextLine().split("-");
		
		
		
		int ans=0;
		
		for(int i=0;i<s.length;i++){
			if(s[i].equals("")) {
				continue;
			}
			String[] strArr = s[i].split("\\+");
			int sum =0;
			 for(String str: strArr ) {
				int tmp = Integer.parseInt(str);
			    sum +=tmp;
			    
			 }
			 if (i==0) {
				 ans+=sum;
			 }
			 else {
				 ans-=sum;
			 }
			 
		}

		System.out.println(ans);
		
		
		
			
		}
		
		
		
		
	

}
