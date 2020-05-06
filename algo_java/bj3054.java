import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj3054 {
	static char[][] peter = { { '.', '.', '#', '.', '.' }, { '.', '#', '.', '#', '.' }, { '#', '.', 'X', '.', '#' },
			{ '.', '#', '.', '#', '.' }, { '.', '.', '#', '.', '.' } };
	static char[][] wendy = { { '.', '.', '*', '.', '.' }, { '.', '*', '.', '*', '.' }, { '*', '.', 'X', '.', '*' },
			{ '.', '*', '.', '*', '.' }, { '.', '.', '*', '.', '.' } };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String tmp = br.readLine();
		char[][] frame = new char[5][1 + 4 * tmp.length()];
		for (int i = 0; i < frame[0].length - 4; i += 4) {
			for (int j = 0; j < 5; j++) {
				for (int k = i; k <= i + 4; k++) {
					frame[j][k] = peter[j][k % 4];
					if (j == 2 && k % 4 == 2)
						frame[j][k] = tmp.charAt(i / 4);
				}
			}
		}
		for (int i = 8; i < frame[0].length - 4; i += 12) {
			for (int j = 0; j < 5; j++) {
				for (int k = i; k <= i + 4; k++) {
					frame[j][k] = wendy[j][k % 4];
					if (j == 2 && k % 4 == 2)
						frame[j][k] = tmp.charAt(i / 4);
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < frame[0].length; j++) {
				sb.append(frame[i][j]);
			}
			sb.append('\n');
		}
		System.out.println(sb.toString());

	}

}
