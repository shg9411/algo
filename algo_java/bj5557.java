package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj5557 {
	static int count;
	static int[] arr;
	static long[][] dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		arr = new int[n];
		for (int i = 0; i < n; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		dp = new long[n][21];
		int tmp;
		dp[0][arr[0]] = 1;
		for (int i = 1; i < n - 1; i++) {
			for (int j = 0; j <= 20; j++) {
				if (dp[i - 1][j] > 0) {
					tmp = j + arr[i];
					if (tmp <= 20 && tmp >= 0)
						dp[i][tmp] += dp[i - 1][j];
					tmp = j - arr[i];
					if (tmp <= 20 && tmp >= 0)
						dp[i][tmp] += dp[i - 1][j];
				}
			}
		}
		System.out.println(dp[n - 2][arr[n - 1]]);

	}

}
