package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj1495 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int[] vol = new int[n];
		for (int i = 0; i < n; i++)
			vol[i] = Integer.parseInt(st2.nextToken());
		int[][] dp = new int[n + 1][m + 1];
		if (s + vol[0] <= m)
			dp[0][s + vol[0]] = 1;
		if (s - vol[0] >= 0)
			dp[0][s - vol[0]] = 1;
		for (int i = 1; i < n; i++) {
			for (int j = 0; j <= m; j++) {
				if (dp[i - 1][j] == 1) {
					if (j + vol[i] <= m)
						dp[i][j + vol[i]] = 1;
					if (j - vol[i] >= 0)
						dp[i][j - vol[i]] = 1;
				}
			}
		}
		for (int i = m; i >= 0; i--)
			if (dp[n - 1][i] == 1) {
				System.out.println(i);
				return;
			}
		System.out.println(-1);

	}

}
