package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj10942 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] board = new int[n + 1];
		int[][] dp = new int[n + 1][n + 1];
		for (int i = 1; i <= n; i++)
			Arrays.fill(dp[i], -1);
		for (int i = 1; i <= n; i++)
			dp[i][i] = 1;
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= n; i++)
			board[i] = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(br.readLine());
		int s, e;
		while (m-- > 0) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			if (dp[s][e] == 1)
				sb.append("1\n");
			else if (dp[s][e] == 0)
				sb.append("0\n");
			else {
				int tmp = s + e;
				boolean x = true;
				for (int i = tmp / 2 + 1; i <= e; i++) {
					if (board[i] == board[tmp - i])
						dp[i][tmp - i] = dp[tmp - i][i] = 1;
					else {
						dp[i][tmp - i] = dp[tmp - i][i] = 0;
						x = false;
						break;
					}
				}
				if (x)
					sb.append("1\n");
				else
					sb.append("0\n");
			}
		}
		System.out.println(sb.toString());

	}

}
