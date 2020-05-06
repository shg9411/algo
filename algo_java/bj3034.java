import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj3034 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());
		int H = Integer.parseInt(st.nextToken());
		double can = Math.sqrt(W*W+H*H);
		while(N-->0) {
			if(can>=Integer.parseInt(br.readLine()))
				bw.append("DA");
			else
				bw.append("NE");
			bw.append('\n');
		}
		bw.flush();
		bw.close();
		br.close();
	}

}
