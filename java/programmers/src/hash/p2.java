package hash;

import java.util.Arrays;


// ������ check�ؾ��Ұ� 
// 1. lambda ������ sort, ���� sort

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
