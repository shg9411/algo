package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj2098 {
	static int n;
	static int[][] w;
	static int[][] dp;
	static int max = 16;
	static int inf = 987654321;

	static int trip(int node, int visit) {
		if (visit == (1 << n) - 1) {
			if (w[node][0] != 0) {
				return w[node][0];
			}
			return inf;
		}
		if (dp[node][visit] != -1) {
			return dp[node][visit];
		}
		int ans = inf;
		for (int next = 0; next < n; next++) {
			if ((visit & (1 << next)) == 0 && w[node][next] > 0) {
				ans = Math.min(ans, trip(next, visit | (1 << next)) + w[node][next]);
			}
		}
		return dp[node][visit] = ans;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		w = new int[max][max];
		dp = new int[max][1 << max];

		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], -1);
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				w[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		System.out.println(trip(0, 1));
	}

}
