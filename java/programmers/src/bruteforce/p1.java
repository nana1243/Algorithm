package brouteforce;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;


// 마져 풀자
public class p1 {

	static int makeScore(int[] pattern, int[] answer) {
		int score = 0;
		for (int i = 0; i < answer.length; i++) {
			int idx = i % pattern.length ;
			if (pattern[idx] == answer[i]) {
				score++;
			}

		}
		return score;
	}

	public static void main(String[] args) {

		int[] answers = {1,2,3,4,5,1,2,2,2,2,2,2,2,2,2,2,3,4};
		int[] ans;

		int[] p1 = { 1, 2, 3, 4, 5 };
		int[] p2 = { 2, 1, 2, 3, 2, 4, 2, 5 };
		int[] p3 = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

		HashMap<Integer, Integer> score = new HashMap<>();

		score.put(1, makeScore(p1, answers));
		score.put(2, makeScore(p2, answers));
		score.put(3, makeScore(p3, answers));
		
		int m = Collections.max(score.values());
		
		
		

}
	
}
