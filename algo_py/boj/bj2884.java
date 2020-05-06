import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj2884 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int H = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int mM = M - 45 < 0 ? M + 15 : M - 45;
		int mH = mM > 14 ? H - 1 : H;
		mH = mH < 0 ? 23 : mH;
		System.out.println(mH + " " + mM);
	}

}
