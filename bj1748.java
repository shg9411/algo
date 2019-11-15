import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj1748 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		int count = 0;
		for (int i = 1; i <= N; i *= 10) {
			count += N - i + 1;
			System.out.println(i + "," + count);
		}

		bw.write(String.valueOf(count));
		bw.flush();
		bw.close();
		br.close();

	}

}
