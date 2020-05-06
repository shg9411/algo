package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj10164 {

	static int findLoad(int i, int j) {
		int[][] dp = new int[i][j];
		for (int x = 0; x < i; x++)
			dp[x][0] = 1;
		for (int y = 0; y < j; y++)
			dp[0][y] = 1;
		for (int x = 1; x < i; x++) {
			for (int y = 1; y < j; y++) {
				dp[x][y] = dp[x - 1][y] + dp[x][y - 1];
			}
		}
		return dp[i - 1][j - 1];
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int x, y, xx, yy;
		if (k != 0) {
			x = k % m == 0 ? k / m : k / m + 1;
			y = k % m == 0 ? m : k % m;
			xx = n - x + 1;
			yy = m - y + 1;
			System.out.println(findLoad(x, y) * findLoad(xx, yy));
		} else {
			System.out.println(findLoad(n, m));
		}
	}

}
