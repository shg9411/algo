import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int l;
	static int c;
	static char[] ans;
	static char[] chr;
	public static void print() {
		for(int k=1; k<=l; k++)
			System.out.print(ans[k]);
		System.out.println();
	}
	public static boolean promising(int i) {
		for(int k=1; k<i; k++) {
			if(ans[i]==ans[k] || ans[i]<ans[k]) //중복이있거나 오름차순이 아닌지 확인
				return false;
		}
		return true;
	}
	public static boolean check() { //모음자음개수 확인
		int a=0,b=0;
		for(int k=1; k<=l; k++) {
			if(ans[k]=='a' || ans[k]=='e' || ans[k]=='o' || ans[k]=='u' || ans[k]=='i')
				a++;
			else
				b++;
			if(a>=1 && b>=2)
				return true;
		}
		return false;
	}
	public static void password(int i) {
		if(promising(i)) {
			if(i==l && check())
				print();
			else if(i<l) {
				for(int k=i+1; k<=c; k++) {
					ans[i+1]=chr[k];
					password(i+1);
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		Scanner sc=new Scanner(System.in);
		l=sc.nextInt();
		c=sc.nextInt();
		ans=new char[l+1];
		chr=new char[c+1];
		chr[0]='A';
		for(int i=1; i<=c; i++) { //c배열  만들기 
			String s=sc.next();
			chr[i]=s.charAt(0);
		}	
		Arrays.sort(chr); 
		for(int i=1; i<=c; i++) {
			ans[1]=chr[i];
			password(1);
		}
	}

}
