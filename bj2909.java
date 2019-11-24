import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj2909 {
	public static void main (String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	
	int C = Integer.parseInt(st.nextToken());
	int K = Integer.parseInt(st.nextToken());
	
	double price = Math.round(C/Math.pow(10, K)) * Math.pow(10, K);
	
	System.out.println((int)price);
	}
}