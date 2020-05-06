import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj5612 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		StringTokenizer st;
		int maxim = m;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int input = Integer.parseInt(st.nextToken());
			int output = Integer.parseInt(st.nextToken());
			m = m + input - output;
			if (m < 0) {
				System.out.println(0);
				return;
			}
			maxim = maxim < m ? m : maxim;
		}
		System.out.println(maxim);
	}

}
