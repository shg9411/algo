import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj1713 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int count = Integer.parseInt(br.readLine());
		int[] student = new int[101];
		Queue<Integer> que = new LinkedList<Integer>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < count; i++) {
			int chu = Integer.parseInt(st.nextToken());
			if (que.contains(chu))
				student[chu]++;
			else if (que.size() >= n) {
				Queue<Integer> tmp = new LinkedList<Integer>();
				int min = que.poll();
				int tmpS = min;
				while (!que.isEmpty()) {
					tmpS = que.poll();
					if (student[min] <= student[tmpS]) {
						tmp.add(tmpS);
					} else {
						tmp.add(min);
						min = tmpS;
					}
				}

				student[min] = 0;
				que = tmp;
				que.offer(chu);
				student[chu]++;
			} else {
				que.offer(chu);
				student[chu]++;
			}
		}
		ArrayList<Integer> al = new ArrayList<Integer>();
		for (Integer it : que)
			al.add(it);
		Collections.sort(al);
		StringBuilder sb = new StringBuilder();
		for (int z = 0; z < al.size(); z++)
			sb.append(al.get(z) + " ");
		System.out.print(sb.toString().trim());

	}

}
