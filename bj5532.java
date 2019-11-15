import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj5532 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int L = Integer.parseInt(br.readLine());
		int A = Integer.parseInt(br.readLine());
		int B = Integer.parseInt(br.readLine());
		double C = Double.parseDouble(br.readLine());
		double D = Double.parseDouble(br.readLine());
		int maxDay = (int) Math.ceil(Math.max(A / C, B / D));
		bw.write(String.valueOf(L - maxDay));
		bw.flush();
		bw.close();
		br.close();
	}
}
