import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj10886 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int flag = 0;
		for (int i = 0; i < N; i++) {
			if (Integer.parseInt(br.readLine()) == 1)
				flag++;
			else
				flag--;
		}
		if (flag > 0)
			System.out.println("Junhee is cute!");
		else
			System.out.println("Junhee is not cute!");
	}

}
