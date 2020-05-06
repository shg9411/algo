package DP;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj1890_bfs {
	static int[][] arr;
	static int n;
	static int count = 0;

	static void bfs() {
		Queue<Point> que = new LinkedList<Point>();
		que.add(new Point(0, 0));
		while (!que.isEmpty()) {
			Point tmp = que.poll();
			int dis = arr[tmp.x][tmp.y];
			if (dis == 0)
				continue;
			int[] disx = { 0, dis };
			int[] disy = { dis, 0 };
			for (int i = 0; i < 2; i++) {
				int nx = tmp.x + disx[i];
				int ny = tmp.y + disy[i];
				if (nx >= n || ny >= n)
					continue;
				if (nx == n - 1 && ny == n - 1) {
					count++;
					continue;
				}
				que.add(new Point(nx, ny));
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		StringTokenizer st;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		bfs();
		System.out.println(count);

	}

}
