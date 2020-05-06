import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj1188 {
	static int gcd(int n, int m) {
		if (m == 0)
			return n;
		return gcd(m, n % m);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] tmp = br.readLine().split(" ");
		int n = Integer.parseInt(tmp[0]);
		int m = Integer.parseInt(tmp[1]);
		System.out.println(m - gcd(n, m));
	}

}
