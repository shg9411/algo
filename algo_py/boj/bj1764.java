import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class bj1764 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		ArrayList<String> noListen = new ArrayList<String>();
		ArrayList<String> noSee = new ArrayList<String>();
		ArrayList<String> noListenSee = new ArrayList<String>();
		while (N-- > 0)
			noListen.add(br.readLine());
		Collections.sort(noListen);
		while (M-- > 0)
			noSee.add(br.readLine());
		Collections.sort(noSee);
		while (noSee.size() > 0 && noListen.size() > 0) {
			if (noSee.get(0).equals(noListen.get(0))) {
				noListenSee.add(noSee.remove(0));
				noListen.remove(0);
			} else if (noSee.get(0).compareTo(noListen.get(0)) > 0) {
				noListen.remove(0);
			} else
				noSee.remove(0);
		}
		System.out.println(noListenSee.size());
		for (String tmp : noListenSee)
			System.out.println(tmp);
	}
}

//Arrays.binarySearch 이진 탐색이라는 중요한 교훈을 얻음
