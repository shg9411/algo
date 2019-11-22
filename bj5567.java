import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj5567 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		final int N = Integer.parseInt(br.readLine());
		final int M = Integer.parseInt(br.readLine());

		boolean[][] friend = new boolean[N + 1][N + 1];
		boolean[] invited = new boolean[N + 1];
		boolean[] myFriend = new boolean[N + 1];

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());

			int tempA = Integer.parseInt(st.nextToken());
			int tempB = Integer.parseInt(st.nextToken());

			friend[tempA][tempB] = true;
			friend[tempB][tempA] = true;
			if (tempA == 1) {
				myFriend[tempB] = true;
				invited[tempB] = true;
			}
		}

		for (int i = 2; i <= N; i++) {
			if (myFriend[i]) {
				for (int j = 0; j < myFriend.length; j++) {
					if (friend[i][j] == true)
						invited[j] = true;
				}
			}
		}

		int count = 0;
		for (int i = 2; i <= N; i++) {
			if (invited[i])
				count++;
		}

		System.out.println(count);
	}
}
