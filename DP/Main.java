package DP;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int N = sc.nextInt();
		int cnt = N;
		if(N<=100) {
		for(int i =0; i<N; i++) {
			int num = sc.nextInt();
			
			if(num>0 &&num<=1000) {
			
				if(num==1) {
				cnt-=1;	
				}else if(num>2 && num%2==0) {
						cnt-=1;
					}else if(num>3 &&num%3==0) {
						cnt-=1;
					}else if(num>5 && num%5==0) {
						cnt-=1;
					}else if(num>7 && num%7==0) {
						cnt-=1;
					}
				}
			
			
			}System.out.println(cnt);
		}
	}
}