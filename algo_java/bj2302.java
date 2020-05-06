package DP;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj2302 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());

		int[] caseArr = new int[N + 1];
		caseArr[0] = 1;
		caseArr[1] = 1;
		for (int i = 2; i <= N; i++) {
			caseArr[i] = caseArr[i - 1] + caseArr[i - 2];
		}

		st = new StringTokenizer(br.readLine());
		int cnt = Integer.parseInt(st.nextToken());
		int temp, pos = 0, result = 1;
		for (int i = 0; i < cnt; i++) { // ù �¼����� VIP, VIP�� VIP ������ ����� �� ���
			st = new StringTokenizer(br.readLine());
			temp = Integer.parseInt(st.nextToken()); // VIP�� ��ȣ
			result = Math.multiplyExact(result, caseArr[temp - 1 - pos]);
			pos = temp;
		}
		result = Math.multiplyExact(result, caseArr[N - pos]); // VIP ~ N�¼� ������ ����� �� ���
		System.out.println(result);
	}
}
