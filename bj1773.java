import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj1773 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int tmp;
		boolean[] count = new boolean[c + 1];
		int countP = 0;
		for (int i = 0; i < n; i++) {
			tmp = Integer.parseInt(br.readLine());
			for (int j = 0; j < count.length; j += tmp) {
				if (!count[j]) {
					count[j] = true;
					countP++;
				}
			}
		}
		bw.write(String.valueOf(countP - 1));
		bw.flush();
		bw.close();
		br.close();

	}

}
