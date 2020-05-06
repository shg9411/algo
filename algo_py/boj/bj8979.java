import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Nation implements Comparable<Nation> {
	int index;
	int gold;
	int silver;
	int bronze;

	public Nation(int g, int s, int b) {
		gold = g;
		silver = s;
		bronze = b;
	}

	@Override
	public int compareTo(Nation o) {
		if (this.gold > o.gold)
			return -1;
		else if (this.gold < o.gold)
			return 1;
		else {
			if (this.silver > o.silver)
				return -1;
			else if (this.silver < o.silver)
				return 1;
			else {
				if (this.bronze > o.bronze)
					return -1;
				else if (this.bronze < o.bronze)
					return 1;
				else {
					return 0;
				}
			}
		}
	}
}

public class bj8979 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int index = 0;
		Nation[] nations = new Nation[N];
		for (int i = 0; i < nations.length; i++) {
			st = new StringTokenizer(br.readLine());
			int tmp = Integer.parseInt(st.nextToken());
			if (tmp == K)
				index = i;
			int g = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			nations[i] = new Nation(g, s, b);
		}
		int rank = 1;
		for (int i = 0; i < nations.length; i++) {
			if (i == index)
				continue;
			if (nations[index].compareTo(nations[i]) == 1) {
				rank++;
			}
		}
		bw.write(String.valueOf(rank));
		bw.flush();
		bw.close();
		br.close();

	}
}
