import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj5596 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = 2;
		int subject;
		int[] score = new int[2];
		StringTokenizer st;
		while (t-- > 0) {
			subject = 4;
			st = new StringTokenizer(br.readLine());
			while (subject-- > 0) {
				score[1 - t] += Integer.parseInt(st.nextToken());
			}
		}
		if (score[0] >= score[1])
			bw.write(String.valueOf(score[0]));
		else
			bw.write(String.valueOf(score[1]));
		bw.flush();
		bw.close();
		br.close();
	}
}
