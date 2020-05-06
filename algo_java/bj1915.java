package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj1915 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int mv = 0;
		int[][] sqare = new int[n][m];
		int[][] dp = new int[n][m];
		String[] tmp;
		for (int i = 0; i < n; i++) {
			tmp = br.readLine().split("");
			for (int j = 0; j < m; j++) {
				sqare[i][j] = Integer.parseInt(tmp[j]);
				dp[i][j] = sqare[i][j];
			}
		}
		for (int i = 1; i < n; i++) {
			for (int j = 1; j < m; j++) {
				int t = dp[i - 1][j - 1];
				if (t >= 1 && sqare[i][j] > 0) {
					int ti = 1;
					while (t >= ti) {
						if (sqare[i - ti][j] == 0 || sqare[i][j - ti] == 0) {
							break;
						}
						dp[i][j]++;
						ti++;
					}
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
//				System.out.print(dp[i][j]);
				if (dp[i][j] > mv)
					mv = dp[i][j];
			}
//			System.out.println();
		}
		System.out.println(mv * mv);

	}

}
