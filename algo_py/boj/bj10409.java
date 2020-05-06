import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj10409 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int T = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int sum = 0;
		int i;
		for (i = 0; i < n; i++) {
			sum += Integer.parseInt(st.nextToken());
			if (sum > T)
				break;
		}
		bw.write(String.valueOf(i));
		bw.flush();
		bw.close();
		br.close();

	}

}
