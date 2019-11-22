import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class bj1722 {
	static int N;
	static long[] arr;

	static long fact(int k) {
		long num = 1;
		for (; k > 1; num *= (k--))
			;
		return num;
	}

	static String getPermutation() {
		StringBuilder sb = new StringBuilder();
		ArrayList<Integer> al = new ArrayList<Integer>();
		int i, j;
		long f, tmp, sum = 0;
		for (i = 1; i <= N; i++)
			al.add(i);
		long index = arr[0] - 1;
		for (i = 1; i < N; i++) {
			for (f = fact(N - i), j = 0;; j++) {
				if ((tmp = sum + j * f) >= index) {
					if (tmp > index) {
						tmp -= f;
						j--;
					}
					sb.append(al.remove(j) + " ");
					sum = tmp;
					break;
				}
			}
		}
		while (!al.isEmpty())
			sb.append(al.remove(0) + " ");
		return sb.toString().trim();
	}

	static String getOrder() {
		int i, j;
		long f, sum = 0;
		ArrayList<Integer> al = new ArrayList<Integer>();
		for (i = 1; i <= N; i++)
			al.add(i);
		for (i = 0; i < N; i++) {
			f = fact(N - i - 1);
			j = al.indexOf((int) arr[i]);
			al.remove(j);
			sum += j * f;
		}
		return (sum + 1) + "";
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());
		String[] stA = br.readLine().split(" ");
		arr = new long[N];
		for (int i = 1; i < stA.length; i++)
			arr[i - 1] = Long.parseLong(stA[i]);

		bw.write(stA[0].equals("1") ? getPermutation() : getOrder());
		bw.close();
		br.close();

	}

}
