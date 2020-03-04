package DP;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String str = scanner.nextLine();
		String[] minusArr = str.split("\\-");
		int result = Integer.parseInt(minusArr[0]);

		for (int i = 1; i < minusArr.length; i++) {
			String[] plusArr = minusArr[i].split("\\+");
			int sum = 0;

			for (int j = 0; j < plusArr.length; j++) {
				sum += Integer.parseInt(plusArr[j]);
			}
			result -= sum;
		}
		System.out.println(result);
		scanner.close();
	}
}
