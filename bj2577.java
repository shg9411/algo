import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj2577 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int A = Integer.parseInt(br.readLine());
		int B = Integer.parseInt(br.readLine());
		int C = Integer.parseInt(br.readLine());
		int[] count = new int[10];
		int val = A * B * C;
		String tmp = String.valueOf(val);
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < tmp.length(); i++)
			count[tmp.charAt(i) - '0']++;
		for (int i = 0; i < 10; i++)
			sb.append(count[i]).append('\n');
		System.out.println(sb);

	}

}
