package DP;

import java.io.IOException;
import java.util.Scanner;
public class test{
	
	public static void main(String args[]) throws IOException{
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		
		int dist = 0;
		int[] arr = new int[51];
		for(int i=0;i<s.length();i++) {
			if(s.charAt(i)=='+' || s.charAt(i)=='-') {
				dist++;
				continue;
			}
			arr[dist]=arr[dist]*10+(s.charAt(i)-'0');
		}
		int sum = arr[0];
		for(int i=1;i<arr.length;i++) {
			sum-=arr[i];
			//System.out.println(arr[i]);
		}
		System.out.println(sum);
	}
}
