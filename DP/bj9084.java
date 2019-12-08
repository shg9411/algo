package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj9084 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int n, m;
		int[] coin, dp;
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		while (t-- > 0) {
			n = Integer.parseInt(br.readLine());
			coin = new int[n + 1];
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= n; i++)
				coin[i] = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(br.readLine());
			dp = new int[m + 1];
			dp[0] = 1;
			for (int i = 1; i <= n; i++) {
				for (int j = coin[i]; j <= m; j++) {
					dp[j] += dp[j - coin[i]];
				}
			}
			sb.append(dp[m] + "\n");
		}
		System.out.println(sb.toString());
	}
}
