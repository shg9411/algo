import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj2804 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] tmp = br.readLine().split(" ");
		int n = tmp[0].length();
		int m = tmp[1].length();
		int answerN = 0;
		int answerM = 0;
		LOOP: for (int i = 0; i < tmp[0].length(); i++) {
			for (int j = 0; j < tmp[1].length(); j++) {
				if (tmp[0].charAt(i) == tmp[1].charAt(j)) {
					answerN = i;
					answerM = j;
					break LOOP;
				}
			}
		}
		for (int i = 0; i < tmp[1].length(); i++) {
			for (int j = 0; j < tmp[0].length(); j++) {
				if (j == answerN)
					bw.append(tmp[1].charAt(i));
				else if (i == answerM)
					bw.append(tmp[0].charAt(j));
				else
					bw.append(".");
			}
			bw.append('\n');
		}
		bw.flush();
		bw.close();
		br.close();
	}

}
