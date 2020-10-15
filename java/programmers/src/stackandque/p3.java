package stackandque;


import java.util.Deque;
import java.util.LinkedList;

public class p3 {

	// 1. 대기트럭에서 한명을 pop
	// 2. 다리를 건너는 트럭에 첨가
	// 2-1. 이때 weight넘으면 안됨
	// 3 . 다리를 지난 트럭에 시간이 되면 넘긴다

	static public int solution(int bridge_length, int weight, int[] truck_weights) {

		Deque<Integer> crossed = new LinkedList<>();
		Deque<int[]> crossing = new LinkedList<>();
		Deque<Integer> waiting = new LinkedList<>();

		for (int elm : truck_weights) {
			waiting.add(elm);
		}

		int time = 1;

		int sum = 0;
		crossing.add(new int[] { waiting.poll(), time });
		sum += crossing.getFirst()[0];

		while (!crossing.isEmpty()) {
			// 빼라
			if (time - crossing.getFirst()[1] == bridge_length - 1) {
				int out = crossing.poll()[0];
				crossed.add(out);
				sum -= out;
			}

			time++;
			if (!waiting.isEmpty() && sum + waiting.getFirst() <= weight) {
				int[] input = { waiting.poll(), time };
				crossing.add(input);
				sum += input[0];
			}

		}

		return time;
	}

	public static void main(String[] args) {

		int bridge_length = 2;
		int weight = 10;
		int[] truck_weights = { 7, 4, 5, 6 };
		int ans = solution(bridge_length, weight, truck_weights);

		System.out.println(ans);

	}

}
