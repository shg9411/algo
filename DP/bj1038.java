package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class bj1038 {
	static Deque<Long> que;
	static int num = 9;

	static long findNum(int i) {
		if (i <= 10)
			return i;
		while (true) {
			long tmp = que.poll();
			long lastnum = tmp % 10;
			for (int k = 0; k < lastnum; k++) {
				que.add(tmp * 10 + k);
				num++;
				if (num >= i)
					return que.getLast();
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		if (n >= 1023) {
			System.out.println(-1);
			return;
		}
		que = new LinkedList<Long>();
		for (long i = 1; i < 10; i++)
			que.add(i);
		System.out.println(findNum(n));
	}

}
