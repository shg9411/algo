import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj5543 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int SB = Integer.parseInt(br.readLine());
		int JB = Integer.parseInt(br.readLine());
		int HB = Integer.parseInt(br.readLine());
		int coke = Integer.parseInt(br.readLine());
		int soda = Integer.parseInt(br.readLine());
		int sum = coke > soda ? soda : coke;
		sum += Math.min(SB, Math.min(JB, HB)) - 50;
		System.out.println(sum);
	}

}
