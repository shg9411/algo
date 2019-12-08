package DP;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj2240 {
	static int stoi(String s) {
		return Integer.parseInt(s);
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int t = stoi(st.nextToken());
		int w = stoi(st.nextToken());

		int[][] dp = new int[t + 1][w + 1];

		for (int i = 1; i <= t; i++) {
			int tree = stoi(br.readLine());

			for (int j = 0; j <= w; j++) {

				if (j == 0) {
					if (tree == 1)
						dp[i][j] = dp[i - 1][j] + 1;
					else
						dp[i][j] = dp[i - 1][j];

					continue;
				}

				if (j % 2 == 0) {
					if (tree == 1)
						dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + 1);
					else
						dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j]);
				}

				else {
					if (tree == 1)
						dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j]);
					else
						dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + 1);
				}
			}
		}

		int ans = 0;
		for (int i = 0; i <= w; i++)
			ans = max(ans, dp[t][i]);

		System.out.println(ans);
	}

	static int max(int a, int b) {
		return (a > b) ? a : b;
	}

}
