import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj2851 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[] mushroom = new int[10];
		int diff = 100;
		int num = 0;
		for (int i = 0; i < mushroom.length; i++)
			mushroom[i] = Integer.parseInt(br.readLine());
		for (int i = 0; i < mushroom.length; i++) {
			for (int j = mushroom.length; j >= i; j--) {
				System.out.println(i + "," + j);
			}
		}
	}

}
