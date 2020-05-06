import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class bj9324 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int tc = Integer.parseInt(br.readLine());
		while (tc-- > 0) {
			HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
			String tmp = br.readLine();
			boolean ok = true;
			for (int i = 0; i < tmp.length(); i++) {
				char tmpC = tmp.charAt(i);
				if (!hm.containsKey(tmpC))
					hm.put(tmpC, 1);
				else {
					if (hm.get(tmpC) % 3 == 2) {
						if (i + 1 == tmp.length()) {
							ok = false;
							break;
						} else if (tmp.charAt(i + 1) != tmpC) {
							ok = false;
							break;
						} else {
							hm.put(tmpC, hm.get(tmpC) + 1);
							i++;
						}
					} else
						hm.put(tmpC, hm.get(tmpC) + 1);
				}
			}
			if (ok)
				sb.append("OK\n");
			else
				sb.append("FAKE\n");
		}
		System.out.println(sb.toString());
	}

}
