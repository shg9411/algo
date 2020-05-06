import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj1924 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		String[] day = { "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" };
		int[] days = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
		if (x == 1) {
			System.out.println(day[(y - 1) % 7]);
		} else {
			int diffM = x - 1;
			int diffD = y - 1;
			int total = 0;
			for (int i = 0; i < diffM; i++)
				total += days[i];
			total += diffD;
			System.out.println(day[total % 7]);
		}

		br.close();
	}
}
