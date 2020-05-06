import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj2839 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] dp = new int[5001];
		Arrays.fill(dp, -1);
		dp[3] = 1;
		dp[5] = 1;
		for (int i = 6; i <= N; i++) {
			int dp_3 = dp[i - 3];
			int dp_5 = dp[i - 5];
			if (dp_3 == -1 && dp_5 == -1)
				dp[i] = -1;
			else if (dp_3 == -1)
				dp[i] = dp_5 + 1;
			else if (dp_5 == -1)
				dp[i] = dp_3 + 1;
			else
				dp[i] = Math.min(dp[i - 3], dp[i - 5]) + 1;
		}
		System.out.println(dp[N]);
	}
}
