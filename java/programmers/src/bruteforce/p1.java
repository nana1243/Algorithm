package bruteforce;

import java.util.HashMap;

public class p1 {

	static int makeScore(int[] pattern, int[] answer) {
		int score = 0;
		for (int i = 0; i < answer.length; i++) {
			int idx = i % pattern.length;
			if (pattern[idx] == answer[i]) {
				score++;
			}

		}
		return score;
	}

	public int[] solution(int[] answers) {

		int[] p1 = { 1, 2, 3, 4, 5 };
		int[] p2 = { 2, 1, 2, 3, 2, 4, 2, 5 };
		int[] p3 = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

		HashMap<Integer, Integer> score = new HashMap<>();

		score.put(1, makeScore(p1, answers));
		score.put(2, makeScore(p2, answers));
		score.put(3, makeScore(p3, answers));

		int m = Math.max(score.get(1), Math.max(score.get(2), score.get(3)));

		if (m == score.get(1) && m == score.get(2) && m == score.get(3)) {
			return new int[] { 1, 2, 3 };

		} else if (m == score.get(1) && m == score.get(2)) {
			return new int[] { 1, 2 };
		} else if (m == score.get(1) && m == score.get(3)) {

			return new int[] { 1, 3 };

		} else if (m == score.get(2) && m == score.get(3)) {
			return new int[] { 2, 3 };

		} else if (m == score.get(1)) {
			return new int[] { 1 };
		} else if (m == score.get(2)) {
			return new int[] { 2 };
		}

		return new int[] { 3 };

	}

	public static void main(String[] args) {
		

	}

}
