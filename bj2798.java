import java.io.*;
import java.util.*;

public class bj2798 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < N; i++) {
			int a = Integer.parseInt(st.nextToken());
			if (a <= M)
				list.add(a);
		}

		Collections.sort(list, Collections.reverseOrder());
		int ans = -1;
		for (int i = 0; i < list.size() - 2; i++) {
			for (int j = i + 1; j < list.size() - 1; j++) {
				for (int k = j + 1; k < list.size(); k++) {
					int chk = list.get(i) + list.get(j) + list.get(k);
					if (chk <= M) {
						ans = Math.max(chk, ans);
					}
				}
			}
		}
		bw.write(ans + "\n");

		bw.flush();
		br.close();
		bw.close();
	}
}