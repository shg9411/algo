import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj2810 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String tmp = br.readLine();
		int count = 1;
		for (int i = 0; i < tmp.length(); i++) {
			if (tmp.charAt(i) != 'S')
				i++;
			count++;
		}
		if (n >= count)
			System.out.println(count);
		else
			System.out.println(n);
	}

}
