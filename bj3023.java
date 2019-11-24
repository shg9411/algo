import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj3023 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		char[][] arr = new char[r * 2][c * 2];
		for (int i = 0; i < r; i++) {
			char[] tmp = br.readLine().toCharArray();
			for (int j = 0; j < tmp.length; j++)
				arr[i][j] = tmp[j];
		}
		for (int i = 0; i < r; i++) {
			for (int j = c; j < arr[0].length; j++) {
				arr[i][j] = arr[i][c * 2 - j - 1];
			}
		}
		for (int i = r; i < r * 2; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				arr[i][j] = arr[r * 2 - i - 1][j];
			}
		}
		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		arr[r-1][c-1] = arr[r-1][c-1] == '.' ? '#' : '.';
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				sb.append(arr[i][j]);
			}
			sb.append('\n');
		}
		System.out.println(sb.toString());

	}

}
