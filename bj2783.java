import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj2783 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(br.readLine());
		int ox, oy;
		double min = (double) x / y;
		double tmp;
		while (n-- > 0) {
			st = new StringTokenizer(br.readLine());
			ox = Integer.parseInt(st.nextToken());
			oy = Integer.parseInt(st.nextToken());
			tmp = (double) ox / oy;
			min = tmp > min ? min : tmp;
		}
		bw.write(String.valueOf(min * 1000));
		bw.close();
		br.close();
	}

}
