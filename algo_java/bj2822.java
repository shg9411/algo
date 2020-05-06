import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class bj2822 {
	static class Score {
		int index;
		int score;

		public Score(int i, int j) {
			this.index = i;
			this.score = j;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Score[] score = new Score[8];
		for (int i = 0; i < score.length; i++) {
			score[i] = new Score(i, Integer.parseInt(br.readLine()));
		}
		Arrays.sort(score, new Comparator<Score>() {
			@Override
			public int compare(Score o1, Score o2) {
				if (o1.score < o2.score)
					return 1;
				else if (o2.score < o1.score)
					return -1;
				return 0;
			}
		});
		int sum = 0;
		ArrayList<Integer> al = new ArrayList<Integer>();
		for (int i = 0; i < 5; i++) {
			sum += score[i].score;
			al.add(score[i].index + 1);
		}
		Collections.sort(al);
		bw.append(String.valueOf(sum)).append('\n');
		for (int i = 0; i < 5; i++)
			bw.append(String.valueOf(al.get(i))).append(" ");
		bw.flush();
		bw.close();
		br.close();
	}
}
