import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class sw8821 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for (int i = 1; i <= t; i++) {
			boolean[] check = new boolean[10];
			String num = br.readLine();
			for (int c = 0; c < num.length(); c++) {
				int tmp = Integer.parseInt(String.valueOf(num.charAt(c)));
				check[tmp] = !check[tmp];
			}
			int count = 0;
			for (int idx = 0; idx < check.length; idx++)
				if (check[idx])
					count++;

			System.out.printf("#%d %d\n", i, count);
		}
	}
}
