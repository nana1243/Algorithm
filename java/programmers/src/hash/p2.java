package hash;

import java.util.Arrays;


// 집가서 check해야할것 
// 1. lambda 식으로 sort, 길이 sort

public class p2 {
	
	 static public boolean solution(String[] phone_book) {
		 Arrays.sort(phone_book);
		 
		 for(int i=0;i<phone_book.length;i++) {
			 for(int j=i+1;j<phone_book.length;j++) {
				 if(phone_book[j].startsWith(phone_book[i])) {
					 return true;
				 }
			 }
		 }
		 return false;
	 }
	
   

	public static void main(String[] args) {
		
		
		String[] phone_book = { "119", "97674223", "1195524421"};
		boolean ans = solution(phone_book);
		System.out.println(ans);

	}

}
