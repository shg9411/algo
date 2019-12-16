import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class sw8741 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		for (int i = 1; i <= tc; i++) {
			String tmp[] = br.readLine().split(" ");
			StringBuilder sb = new StringBuilder();
			for (int l = 0; l < tmp.length; l++)
				sb.append(Character.toUpperCase(tmp[l].charAt(0)));
			System.out.printf("#%d %s\n", i, sb.toString());
		}
	}
}
