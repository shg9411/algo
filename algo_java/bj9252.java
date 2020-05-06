package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj9252 {
	static int[][] dp;
	static String f, s;
	static StringBuilder sb = new StringBuilder();

	static void backTracking(int m, int n) {
		if (m == 0 || n == 0)
			return;
		if (dp[m][n] > dp[m - 1][n - 1] && dp[m][n] > dp[m - 1][n] && dp[m][n] > dp[m][n - 1]) {
			sb.insert(0, s.charAt(n - 1));
			backTracking(m - 1, n - 1);
		} else if (dp[m][n] > dp[m - 1][n] && dp[m][n] == dp[m][n - 1])
			backTracking(m, n - 1);
		else
			backTracking(m - 1, n);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		f = br.readLine();
		s = br.readLine();
		dp = new int[f.length() + 1][s.length() + 1];
		for (int i = 1; i < dp.length; i++) {
			for (int j = 1; j < dp[i].length; j++) {
				if (f.charAt(i - 1) == s.charAt(j - 1))
					dp[i][j] = dp[i - 1][j - 1] + 1;
				else
					dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
		backTracking(f.length(), s.length());
		System.out.println(dp[f.length()][s.length()]);
		System.out.println(sb.toString());
	}

}
