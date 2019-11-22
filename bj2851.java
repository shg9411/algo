import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj2851 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[] score = new int[10];
		for (int i = 0; i < 10; i++)
			score[i] = Integer.parseInt(br.readLine());
		int sum = 0;
		int num = 100;
		int diff = sum - num;
		int tmp;
		for (int i = 0; i < score.length; i++) {
			sum = 0;
			for (int j = 0; j <= i; j++) {
				sum += score[j];
			}
			tmp = sum - num;
			if (Math.abs(tmp) < Math.abs(diff))
				diff = tmp;
			else if (Math.abs(tmp) == Math.abs(diff))
				diff = tmp > diff ? tmp : diff;
		}
		bw.write(String.valueOf(num+diff));
		bw.flush();
		bw.close();
		br.close();
	}
}
