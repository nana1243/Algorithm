package dfsbfs;

public class p1 {
	static int n;
	static int answer;
	static int[] numbers;
	static int target;

	static void dfs(int idx, int value) {
			if (idx==n-1) {
				if(value == target) {
					answer+=1;
				}
				return;
			}
			
			dfs(idx+1, value+numbers[idx+1]);
			dfs(idx+1,value-numbers[idx+1]);
			
			
		}

	public static void main(String[] args) {

		numbers = new int[] { 1, 1, 1, 1, 1 };
		target = 3;
		n = numbers.length;

		dfs(0, numbers[0]);
		dfs(0, -numbers[0]);

		System.out.println(answer);

	}

}
