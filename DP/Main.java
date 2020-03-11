package DP;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
	static HashMap<String, String[]> map = new HashMap<String, String[]>();
	static int ans = 1;

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		long ln = 0;
		String str = "";
		String[] strArr;
		for (int i = 0; i < n; i++) {
			str = sc.next();
			ln = sc.nextLong();
			strArr = new String[ln];
			for (int j = 0; j < ln; j++) {
				strArr[j] = sc.next();
			}
			map.put(str, strArr);
		}
		String target = sc.next();
		solution(map.get(target));
		System.out.println(ans);

	}

	public static void solution(String[] arr) {
		for (int i = 0; i < arr.length; i++) {
			ans++;
			if (!map.containsKey(arr[i])) {
				continue;
			}
			solution(map.get(arr[i]));
		}
	}
}