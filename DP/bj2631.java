package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj2631 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] chil = new int[n];
		int[] dp = new int[n];
		for (int i = 0; i < n; i++)
			chil[i] = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			if (dp[i] == 0)
				dp[i] = 1;
			for (int j = 0; j < i; j++) {
				if (chil[i] > chil[j]) {
					if (dp[i] < dp[j] + 1)
						dp[i] = dp[j] + 1;
				}
			}
		}
		System.out.println(n - Arrays.stream(dp).max().getAsInt());
	}

}
