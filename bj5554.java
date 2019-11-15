import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj5554 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int sum = 0;
		int count = 4;
		while (count-- > 0)
			sum += Integer.parseInt(br.readLine());
		bw.append(String.valueOf(sum / 60)).append('\n');
		sum %= 60;
		bw.append(String.valueOf(sum));
		bw.flush();
		bw.close();
		br.close();
	}
}
