import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj2490 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] yut = { "E", "A", "B", "C", "D" };
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 3; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int count = 0;
			while (st.hasMoreTokens())
				if (Integer.parseInt(st.nextToken()) == 0)
					count++;
			sb.append(yut[count]).append('\n');
		}
		System.out.println(sb);
	}

}
