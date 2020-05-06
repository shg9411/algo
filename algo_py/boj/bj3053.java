import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj3053 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int R = Integer.parseInt(br.readLine());
		double you = R * R * Math.PI;
		double taxi = R * R * 2;
		System.out.printf("%.6f\n", you);
		System.out.printf("%.6f", taxi);
	}
}
