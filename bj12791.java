import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class bj12791 {

	public static void main(String[] args) throws IOException {
		Map<Integer, ArrayList<String>> map = new HashMap<>();
		String tmp = "1967 DavidBowie\r\n" + "1969 SpaceOddity\r\n" + "1970 TheManWhoSoldTheWorld\r\n"
				+ "1971 HunkyDory\r\n" + "1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars\r\n"
				+ "1973 AladdinSane\r\n" + "1973 PinUps\r\n" + "1974 DiamondDogs\r\n" + "1975 YoungAmericans\r\n"
				+ "1976 StationToStation\r\n" + "1977 Low\r\n" + "1977 Heroes\r\n" + "1979 Lodger\r\n"
				+ "1980 ScaryMonstersAndSuperCreeps\r\n" + "1983 LetsDance\r\n" + "1984 Tonight\r\n"
				+ "1987 NeverLetMeDown\r\n" + "1993 BlackTieWhiteNoise\r\n" + "1995 1.Outside\r\n"
				+ "1997 Earthling\r\n" + "1999 Hours\r\n" + "2002 Heathen\r\n" + "2003 Reality\r\n"
				+ "2013 TheNextDay\r\n" + "2016 BlackStar";
		String[] tmpA = tmp.split(" |\r\n");
		for (int i = 0; i < tmpA.length - 1; i += 2) {
			if (!map.containsKey(Integer.parseInt(tmpA[i]))) {
				ArrayList<String> al = new ArrayList<String>();
				al.add(tmpA[i + 1]);
				map.put(Integer.parseInt(tmpA[i]), al);
			} else {
				ArrayList<String> al = map.get(Integer.parseInt(tmpA[i]));
				al.add(tmpA[i + 1]);
				map.put(Integer.parseInt(tmpA[i]), al);
			}
		}
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int Q = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int from, to, count;
		while (Q-- > 0) {
			st = new StringTokenizer(br.readLine());
			count = 0;
			from = Integer.parseInt(st.nextToken());
			to = Integer.parseInt(st.nextToken());
			StringBuilder tsb = new StringBuilder();
			for (int i = from; i <= to; i++) {
				if (map.containsKey(i)) {
					ArrayList<String> tal = map.get(i);
					count += tal.size();
					for (String tst : tal)
						tsb.append(i).append(" ").append(tst).append('\n');
				}
			}
			if (count == 0)
				sb.append(count).append('\n');
			else
				sb.append(count).append('\n').append(tsb);
		}
		System.out.println(sb.toString());

	}

}
