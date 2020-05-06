import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class bj4153 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			ArrayList<Integer> al = new ArrayList<Integer>();
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			if (x == 0 && y == 0 && z == 0)
				break;
			al.add(x);
			al.add(y);
			al.add(z);
			Collections.sort(al);
			if (Math.pow(al.get(2), 2) == Math.pow(al.get(1), 2) + Math.pow(al.get(0), 2))
				bw.write("right\n");
			else
				bw.write("wrong\n");
		}
		br.close();
		bw.flush();
		bw.close();
	}
}
