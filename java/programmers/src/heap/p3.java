package heap;

import java.util.Comparator;
import java.util.PriorityQueue;


public class p3 {

	static PriorityQueue<Integer> min;
	static PriorityQueue<Integer> max;

	public static void rule(String[] command) {
		System.out.println(min);
		System.out.println(max);
		

		if (command[0].equals("D")) {
			if (command[1].equals("1") && !(min.isEmpty() && max.isEmpty())) {
				int out = max.poll();
				min.remove(out);
			} else if(command[1].equals("-1") && !(min.isEmpty() && max.isEmpty())){
				
				int out = min.poll();
				max.remove(out);

			}

		} else {
			int put = Integer.parseInt(command[1]);
			max.add(put);
			min.add(put);

		}

	}

	public static void main(String[] args) {

		max = new PriorityQueue<Integer>(new Comparator<Integer>() {
			public int compare(Integer o1, Integer o2) {

				if (o1 < o2) {
					return 1;
				}
				return -1;
			};
		});

		min = new PriorityQueue<Integer>(new Comparator<Integer>() {
			public int compare(Integer o1, Integer o2) {

				if (o1 < o2) {
					return -1;
				}
				return 1;
			};
		});
		
		
		
		
		String[] operations =  {"I 7","I 5","I -5","D -1"};
		
		for(String elm : operations) {
			String[] command = elm.split(" ");
			rule(command);
		}
		
		int res1 =0;
		int res2 =0;
		if(!max.isEmpty()) {
			res1 += max.poll();
		}
		if(!min.isEmpty()) {
			res2 += min.poll();
		}
		

	}

}
