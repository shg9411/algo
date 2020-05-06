package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj6359 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		while (t-- > 0) {
			int tmp = Integer.parseInt(br.readLine());
			int count = 0;
			boolean[] z = new boolean[tmp + 1];
			for (int i = 2; i <= tmp; i++) {
				for (int j = i; j <= tmp; j += i)
					z[j] = !z[j];
			}
			for (int i = 1; i <= tmp; i++) {
				if (!z[i])
					count++;
			}
			System.out.println(count);
		}
	}

}
