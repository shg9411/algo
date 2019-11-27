package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj2133 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] dp = new int[31];
		dp[0] = 1;
		dp[2] = 3;
		for (int i = 4; i < 31; i += 2) {
			dp[i] = dp[i - 2] * 3;
			for (int j = 4; i - j >= 0; j += 2)
				dp[i] += dp[i - j] * 2;
		}

		System.out.println(dp[n]);
	}

}
