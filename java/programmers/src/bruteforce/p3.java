package brouteforce;

import java.util.ArrayList;
import java.util.Arrays;

public class p3 {

	public static void main(String[] args) {
		int brown = 10;
		int yellow = 2;
		int[] answer = new int[2];
		
		int by = brown + yellow;
		ArrayList<int[]> candidate = new ArrayList<int[]>();
		
		
		for( int i=1;i<by;i++) {
			if(by%i==0 && by/i>=i) {
				int[] tmp=  {by/i,i};
				candidate.add(tmp);
			}
		}
		
		for(int[] elm: candidate) {
			if((( elm[0]-2)*(elm[1]-2))==yellow) {
				answer[0] = elm[0];
				answer[1] = elm[1];
				break;
			}
		}
		System.out.println(Arrays.toString(answer));
		
	}

}
