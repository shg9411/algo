package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj1965 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] box = new int[n];
		int[] dp = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < box.length; i++)
			box[i] = Integer.parseInt(st.nextToken());
		int max = 0;
		for (int i = 0; i < box.length; i++) {
			dp[i] = 1;
			for (int j = 0; j < i; j++) {
				if (box[j] < box[i] && dp[i] < dp[j] + 1)
					dp[i] = dp[j] + 1;
			}
			if (max < dp[i])
				max = dp[i];
		}
		System.out.println(max);
	}

}
