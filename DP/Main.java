package DP;

import java.util.Arrays;

class Test {
	int kth(int[] a, int k) {
        Arrays.sort(a);
        return a[k-1];
    }
}
public class Main {
	public static void main(String args[]) {
		int[] a = {3,4,69143,134,5463456};
		int k = 1;
		System.out.print(new Test().kth(a, k));
	}
}