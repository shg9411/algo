import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj4948 {
	static void sosu(int n) {
		int count = 0;
		if (n == 1) {
			System.out.println(1);
			return;
		}
		for (int i = n+1; i <= 2 * n; i++) {
			boolean flag = true;
			for (int j = 2; j <= Math.sqrt(i); j++) {
				if (i % j == 0) {
					flag = false;
					break;
				}
			}
			if (flag)
				count++;

		}
		System.out.println(count);
		return;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tmp;
		while ((tmp = Integer.parseInt(br.readLine())) != 0)
			sosu(tmp);

	}

}
