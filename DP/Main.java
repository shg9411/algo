package DP;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static int arr[][];
	static int dx[] = { -1, 0, 1, 0 };
	static int dy[] = { 0, 1, 0, -1, };
	static boolean visit[][];
	static int color;
	static int size;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		size = Integer.parseInt(sc.nextLine());
		arr = new int[size][size];
		visit = new boolean[size][size];
		color = 0;
		ArrayList<Integer> a = new ArrayList<Integer>();
		for (int i = 0; i < size; i++) {
			String s = sc.nextLine();
			for (int j = 0; j < size; j++) {
				arr[i][j] = s.charAt(j) - '0';
			}
		}

		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				if (arr[i][j] == 1 && visit[i][j] == false) {
					color++;
					visit[i][j] = true;
					arr[i][j] = color;
					DFS(i, j);
				}
			}
		}

		// Ãâ·Â
		System.out.println(color);
		int count[] = new int[color + 1];
		for (int i = 1; i <= color; i++) {
			for (int j = 0; j < size; j++) {
				for (int k = 0; k < size; k++) {
					if (arr[j][k] == i) {
						count[i]++;
					}
				}
			}
		}
		Arrays.sort(count);
		for (int i = 1; i <= color; i++) {
			System.out.println(count[i]);
		}

	}

	private static void DFS(int xx, int yy) {
		visit[xx][yy] = true;
		int x = xx;
		int y = yy;
		for (int i = 0; i < 4; i++) {
			int rx = x + dx[i];
			int ry = y + dy[i];
			if (rx < 0 || ry < 0 || rx >= size || ry >= size || arr[rx][ry] == 0) {
				continue;
			}
			if (visit[rx][ry] == true) {
				continue;
			}
			if (arr[rx][ry] == 1) {
				arr[rx][ry] = color;
				DFS(rx, ry);
			}
		}

	}

}
