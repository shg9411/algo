package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj11054 {
	static int[] arr;
	static int[] dp;
	static int[] dp1;
	static int[] dp2;
	static int n;

	static void lis() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				if (arr[i] > arr[j]) {
					if (dp1[i] < dp1[j] + 1)
						dp1[i] = dp1[j] + 1;
				}
			}
		}
	}

	static void reverse() {
		for (int i = n - 1; i >= 0; i--) {
			for (int j = n - 1; j >= i; j--) {
				if (arr[j] < arr[i]) {
					if (dp2[i] < dp2[j] + 1)
						dp2[i] = dp2[j] + 1;
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		arr = new int[n];
		dp = new int[n];
		dp1 = new int[n];
		dp2 = new int[n];
		Arrays.fill(dp1, 1);
		Arrays.fill(dp2, 1);
		for (int i = 0; i < n; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		lis();
		reverse();
		for (int i = 0; i < n; i++)
			dp[i] = dp1[i] + dp2[i] - 1;
		System.out.println(Arrays.stream(dp).max().getAsInt());

	}

}
