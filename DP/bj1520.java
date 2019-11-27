package DP;

import java.io.*;
import java.util.*;

public class bj1520 {

	static int m, n;
	static int[][] map;
	static int[][] memo;

	public static void main(String[] args) {
		InputReader in = new InputReader(System.in);
		PrintWriter out = new PrintWriter(System.out);

		m = in.nextInt();
		n = in.nextInt();
		map = new int[m][n];
		memo = new int[m][n];
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				map[i][j] = in.nextInt();
			}
		}
		for (int[] a : memo) {
			Arrays.fill(a, -1);
		}
		System.out.println(path(0, 0));

		out.close();
	}

	static int path(int i, int j) {
		if (i == m - 1 && j == n - 1)
			return 1;
		if (memo[i][j] != -1)
			return memo[i][j];
		int ret = 0;
		if (i + 1 < m && map[i + 1][j] < map[i][j])
			ret += path(i + 1, j);
		if (j + 1 < n && map[i][j + 1] < map[i][j])
			ret += path(i, j + 1);
		if (i - 1 >= 0 && map[i - 1][j] < map[i][j])
			ret += path(i - 1, j);
		if (j - 1 >= 0 && map[i][j - 1] < map[i][j])
			ret += path(i, j - 1);
		return memo[i][j] = ret;
	}
}

class InputReader {

	private final InputStream stream;
	private final byte[] buf = new byte[8192];
	private int curChar, snumChars;

	public InputReader(InputStream st) {
		this.stream = st;
	}

	public int read() {
		if (snumChars == -1)
			throw new InputMismatchException();
		if (curChar >= snumChars) {
			curChar = 0;
			try {
				snumChars = stream.read(buf);
			} catch (IOException e) {
				throw new InputMismatchException();
			}
			if (snumChars <= 0)
				return -1;
		}
		return buf[curChar++];
	}

	public int nextInt() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		int res = 0;
		do {
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}

	public long nextLong() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		long res = 0;
		do {
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}

	public int[] nextIntArray(int n) {
		int a[] = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = nextInt();
		}
		return a;
	}

	public String readString() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		StringBuilder res = new StringBuilder();
		do {
			res.appendCodePoint(c);
			c = read();
		} while (!isSpaceChar(c));
		return res.toString();
	}

	public String nextLine() {
		int c = read();
		while (isSpaceChar(c))
			c = read();
		StringBuilder res = new StringBuilder();
		do {
			res.appendCodePoint(c);
			c = read();
		} while (!isEndOfLine(c));
		return res.toString();
	}

	public boolean isSpaceChar(int c) {
		return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
	}

	private boolean isEndOfLine(int c) {
		return c == '\n' || c == '\r' || c == -1;
	}

}