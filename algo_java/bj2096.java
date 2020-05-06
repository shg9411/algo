package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj2096 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] arr = new int[n][3];
		int[][] max = new int[n][3];
		int[][] min = new int[n][3];
		StringTokenizer st;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int mv1, mv2, miv1, miv2;
		max[0] = min[0] = arr[0];
		for (int i = 1; i < n; i++) {
			mv1 = Math.max(max[i - 1][0], max[i - 1][1]);
			mv2 = Math.max(max[i - 1][2], max[i - 1][1]);
			miv1 = Math.min(min[i - 1][0], min[i - 1][1]);
			miv2 = Math.min(min[i - 1][2], min[i - 1][1]);
			max[i][0] = arr[i][0] + mv1;
			max[i][2] = arr[i][2] + mv2;
			max[i][1] = arr[i][1] + Math.max(mv1, mv2);

			min[i][0] = arr[i][0] + miv1;
			min[i][2] = arr[i][2] + miv2;
			min[i][1] = arr[i][1] + Math.min(miv1, miv2);
		}

		int maxv = Arrays.stream(max[n - 1]).max().getAsInt();
		int minv = Arrays.stream(min[n - 1]).min().getAsInt();
		System.out.println(maxv + " " + minv);
	}

}
