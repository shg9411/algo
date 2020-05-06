package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj11066 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int k;
		int[] arr;
		int[] sum;
		int[][] dp;
		while (t-- > 0) {
			k = Integer.parseInt(br.readLine());
			arr = new int[k + 1];
			sum = new int[k + 1];
			dp = new int[k + 1][k + 1];
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= k; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
				sum[i] = sum[i - 1] + arr[i];
			}
			for (int i = 1; i < k; i++) {
				for (int tx = 1; tx + i <= k; tx++) {
					int ty = tx + i;
					dp[tx][ty] = Integer.MAX_VALUE;
					for (int mid = tx; mid < ty; mid++)
						dp[tx][ty] = Math.min(dp[tx][ty], dp[tx][mid] + dp[mid + 1][ty] + sum[ty] - sum[tx - 1]);
				}
			}
			sb.append(dp[1][k]).append('\n');
		}
		System.out.println(sb.toString());
	}
}
