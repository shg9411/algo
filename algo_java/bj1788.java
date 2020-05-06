import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj1788 {
	static StringBuilder sb;
	static int[] fib;

	static void fibo(int f) {
		f = Math.abs(f);
		if (f == 0) {
			sb.append("0");
			return;
		} else if (f == 1) {
			sb.append("1");
			return;
		}
		fib[0] = 0;
		fib[1] = 1;
		for (int i = 2; i <= f; i++) {
			fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000000;
		}
		sb.append(fib[f]);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		fib = new int[Math.abs(n) + 1];
		sb = new StringBuilder();
		if (n == 0)
			sb.append("0\n");
		else if (n > 0)
			sb.append("1\n");
		else {
			if (n % 2 == 0)
				sb.append("-1\n");
			else
				sb.append("1\n");
		}
		fibo(n);
		System.out.println(sb.toString());
	}

}
