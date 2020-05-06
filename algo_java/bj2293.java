package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj2293 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int[] coin = new int[n];
		int[] dp = new int[k + 1];
		for (int i = 0; i < coin.length; i++) {
			coin[i] = Integer.parseInt(br.readLine());
		}
		dp[0] = 1;
		for (int i = 0; i < coin.length; i++) {
			for (int j = 1; j <= k; j++) {
				if (j - coin[i] >= 0)
					dp[j] += dp[j - coin[i]];
			}
		}
		System.out.println(dp[k]);
	}
}
