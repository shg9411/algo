import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj5032 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int voidCan = Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
		int devide = Integer.parseInt(st.nextToken());
		int can = 0;
		int tmp;
		while (voidCan >= devide) {
			tmp = voidCan / devide;
			can += tmp;
			voidCan = voidCan % devide + tmp;
		}
		bw.append(String.valueOf(can));
		bw.flush();
		bw.close();
		br.close();

	}
}
