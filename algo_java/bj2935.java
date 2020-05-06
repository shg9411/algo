import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj2935 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String A = br.readLine();
		String op = br.readLine();
		String B = br.readLine();
		int a = A.length();
		int b = B.length();
		if (op.equals("+")) {
			if (a == b)
				bw.append(A.replace('1', '2'));
			else if (a > b) {
				bw.append(A.substring(0, a - b));
				bw.append(B);
			} else {
				bw.append(B.substring(0, b - a));
				bw.append(A);
			}
		} else {
			bw.append("1");
			for (int i = 2; i < a + b; i++)
				bw.append("0");
		}
		bw.flush();
		bw.close();
		br.close();

	}
}
