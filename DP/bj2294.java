package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj2294 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int[] coin = new int[n];
		int[] dp = new int[k + 1];
		Arrays.fill(dp, 100001);
		dp[0] = 0;
		for (int i = 0; i < coin.length; i++)
			coin[i] = Integer.parseInt(br.readLine());
		for (int i = 0; i < coin.length; i++) {
			for (int j = coin[i]; j < dp.length; j++) {
				dp[j] = Math.min(dp[j], dp[j - coin[i]] + 1);
			}
		}
		if (dp[k] == 100001)
			System.out.println(-1);
		else
			System.out.println(dp[k]);

	}

}
