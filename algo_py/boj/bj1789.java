import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj1789 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Long S = Long.parseLong(br.readLine());
		br.close();
		int count = 0;
		int current = 1;
		while (S >= current) {
			if (S - current >= 0) {
				S = S - current;
				count++;
			}
			current++;
		}
		bw.write(String.valueOf(count));
		bw.flush();
		bw.close();
	}
}
