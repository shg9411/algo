package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj9507 {
	static long[] fibo;

	static long koong(int n) {
		if (fibo[n] == 0)
			fibo[n] = koong(n - 1) + koong(n - 2) + koong(n - 3) + koong(n - 4);
		return fibo[n];
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		fibo = new long[68];
		fibo[0] = fibo[1] = 1;
		fibo[2] = 2;
		fibo[3] = 4;
		StringBuilder sb = new StringBuilder();
		int tmp;
		while (tc-- > 0) {
			tmp = Integer.parseInt(br.readLine());
			sb.append(koong(tmp)).append("\n");
		}
		System.out.println(sb.toString());
	}

}
