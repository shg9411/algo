import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj2033 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int count = 0;
		StringBuilder sb = new StringBuilder();
		while (true) {
			if (n / 10 > 0) {
				n = (int) (Math.round(n / 10.0));
				count++;
			} else
				break;
		}
		sb.append(n);
		for (int i = 0; i < count; i++)
			sb.append("0");
		System.out.println(sb.toString());
	}

}
