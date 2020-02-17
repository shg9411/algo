package DP;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	private static boolean[] isCut;
	private static int[] visitedOrder;
	private static ArrayList<Integer>[] array;
	private static int count = 0;

	private static int dfs(int here, boolean isRoot) {
		visitedOrder[here] = ++count;
		int result = visitedOrder[here];

		int child = 0;

		for (int next : array[here]) {
			if (visitedOrder[next] != 0) {
				result = Math.min(result, visitedOrder[next]);
				continue;
			}

			child++;
			int prev = dfs(next, false);

			if (!isRoot && prev >= visitedOrder[here]) {
				isCut[here] = true;
			}
		}

		if (isRoot) {
			if (child >= 2) {
				isCut[here] = true;
			}
		}
		return result;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int v = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());

		visitedOrder = new int[v + 1];
		isCut = new boolean[v + 1];
		array = new ArrayList[v + 1];
		for (int i = 1; i <= v; i++) {
			array[i] = new ArrayList<>();
		}

		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(bf.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			array[a].add(b);
			array[b].add(a);
		}

		for (int i = 1; i <= v; i++) {
			if (visitedOrder[i] == 0) {
				dfs(i, true);
			}
		}

		int cnt = 0;
		for (int i = 1; i <= v; i++) {
			if (isCut[i])
				cnt++;
		}
		bw.write(cnt + "\n");

		for (int i = 1; i <= v; i++) {
			if (isCut[i]) {
				sb.append(i + " ");
			}
		}
		sb.delete(sb.length() - 1, sb.length());
		bw.write(sb.toString());
		bw.flush();
	}
}