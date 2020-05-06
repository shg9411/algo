import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj10984 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		int stat;
		double sum;
		double ave;
		int tmp;
		StringTokenizer st;
		while (T-- > 0) {
			int N = Integer.parseInt(br.readLine());
			stat = 0;
			sum = 0.0;
			while (N-- > 0) {
				st = new StringTokenizer(br.readLine());
				tmp = Integer.parseInt(st.nextToken());
				sum += Double.parseDouble(st.nextToken()) * tmp;
				stat += tmp;
			}
			ave = sum / stat;
			System.out.printf("%d %.1f\n", stat, ave);
		}
		br.close();
	}
}
