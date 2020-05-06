import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj2986 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int i;
		for (i = n / 2; i >= 1; i--) {
			if (n % i == 0)
				break;
		}
		System.out.println(n - i);

	}

}
