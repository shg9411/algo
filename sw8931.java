import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class sw8931 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		int ic, result, input;
		for (int i = 1; i <= tc; i++) {
			ic = Integer.parseInt(br.readLine());
			result = 0;
			Stack<Integer> st = new Stack<Integer>();
			while (ic-- > 0) {
				input = Integer.parseInt(br.readLine());
				if (input == 0)
					st.pop();
				else
					st.push(input);
			}
			while (!st.empty())
				result += st.pop();
			System.out.printf("#%d "+result,i);
			System.out.println();
		}
	}

}
