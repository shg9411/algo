package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj1010 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		int west, east;
		int[][] dp;
		while (t-- > 0) {
			st = new StringTokenizer(br.readLine());
			west = Integer.parseInt(st.nextToken());
			east = Integer.parseInt(st.nextToken());
			dp = new int[west + 1][east + 1];
			for (int i = 0; i <= east; i++)
				dp[1][i] = i;
			for (int i = 2; i <= west; i++) {
				for (int j = i; j <= east; j++) {
					for (int k = j; k >= i; k--) {
						dp[i][j] += dp[i - 1][k - 1];
					}
				}
			}
			System.out.println(dp[west][east]);
		}
	}
}
