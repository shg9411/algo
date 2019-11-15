import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj2563 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		boolean[][] white = new boolean[101][101];
		int N = Integer.parseInt(br.readLine());
		int count = 0;
		while (N-- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int X = Integer.parseInt(st.nextToken());
			int Y = Integer.parseInt(st.nextToken());
			for (int i = X; i < X + 10; i++)
				for (int j = Y; j < Y + 10; j++) {
					if (!white[i][j]) {
						white[i][j] = true;
						count++;
					}
				}
		}
		bw.write(String.valueOf(count));
		bw.flush();
		br.close();
		bw.close();
	}
}
