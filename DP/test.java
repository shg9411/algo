package DP;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class test {
	private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String args[]) throws IOException {
		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			int n = Integer.parseInt(br.readLine());
			long[] DP = new long[n + 1];

			for (int j = 0; j <= n; j++)
				DP[j] = solve(j);

			bw.write(Long.toString(DP[n])+'\n');
			bw.flush();
		}
	}

	public static int solve(int n) {
		if (n < 0)
			return 0;
		if (n == 0)
			return 1;

		return solve(n - 1) + solve(n - 2) + solve(n - 3);
	}
}