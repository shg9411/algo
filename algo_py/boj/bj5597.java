import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj5597 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		boolean[] arr = new boolean[30];
		for (int i = 0; i < 28; i++)
			arr[Integer.parseInt(br.readLine()) - 1] = true;
		for (int i = 0; i < 30; i++)
			if (!arr[i])
				bw.append(String.valueOf(i + 1)).append('\n');

		bw.flush();
		bw.close();
		br.close();
	}
}
