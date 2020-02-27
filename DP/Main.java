package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] array = new String[n];
		for (int i = 0; i < array.length; i++) {

			array[i] = br.readLine();
		}
		Arrays.sort(array, new Comparator<String>() {
			@Override
			public int compare(String s1, String s2) {
				if (s1.length() < s2.length()) {
					return -1;
				} else if (s1.length() > s2.length()) {
					return 1;
				} else {
					String tmp1 = s1;
					s1 = s1.replaceAll("[^0-9]", "");
					int[] arr1 = new int[s1.length()];
					int result1 = 0;
					for (int i = 0; i < arr1.length; i++) {
						result1 += (s1.charAt(i) - '0');
					}
					String tmp2 = s2;
					s2 = s2.replaceAll("[^0-9]", "");
					int[] arr2 = new int[s2.length()];
					int result2 = 0;
					for (int i = 0; i < arr2.length; i++) {
						result2 += (s2.charAt(i) - '0');
					}
					if (result1 > result2) {
						return 1;
					} else if (result1 < result2) {
						return -1;
					} else {
						return tmp1.compareTo(tmp2);
					}
				}
			}
		});
		for (int i = 0; i < array.length; i++) {
			System.out.println(array[i]);
		}
	}

}