import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj5565 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int total = Integer.parseInt(br.readLine());
		for (int i = 0; i < 9; i++)
			total -= Integer.parseInt(br.readLine());
		System.out.println(total);
	}
}
