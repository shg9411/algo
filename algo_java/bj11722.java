package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj11722 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[a];
		int[] dp = new int[a];
		for (int i = 0; i < a; i++)
			arr[i] = Integer.parseInt(st.nextToken());

		for (int i = 0; i < a; i++) {
			dp[i] = 1;
			for (int j = 0; j < i; j++) {
				if (arr[i] < arr[j] && dp[j] + 1 > dp[i])
					dp[i] = dp[j] + 1;
			}
		}
		System.out.println(Arrays.stream(dp).max().getAsInt());
	}

}
