package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj5582 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String f = br.readLine();
		String s = br.readLine();
		int[][] arr = new int[f.length() + 1][s.length() + 1];
		int mv = 0;
		for (int i = 1; i <= f.length(); i++) {
			for (int j = 1; j <= s.length(); j++) {
				if (f.charAt(i - 1) == s.charAt(j - 1)) {
					arr[i][j] = arr[i - 1][j - 1] + 1;
					if (mv < arr[i][j])
						mv = arr[i][j];
				}
			}
		}
		System.out.println(mv);

	}

}
