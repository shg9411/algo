import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class bj12790 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		int HP, MP, attack, depence, stat;
		while (T-- > 0) {
			st = new StringTokenizer(br.readLine());
			HP = Integer.parseInt(st.nextToken());
			MP = Integer.parseInt(st.nextToken());
			attack = Integer.parseInt(st.nextToken());
			depence = Integer.parseInt(st.nextToken());
			HP += Integer.parseInt(st.nextToken());
			MP += Integer.parseInt(st.nextToken());
			attack += Integer.parseInt(st.nextToken());
			depence += Integer.parseInt(st.nextToken());
			HP = HP < 1 ? 1 : HP;
			MP = MP < 1 ? 1 : MP;
			attack = attack < 0 ? 0 : attack;
			stat = HP + 5 * MP + 2 * attack + 2 * depence;
			bw.append(String.valueOf(stat)).append('\n');
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
