package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] tmp = br.readLine().toCharArray();
		String bomb = br.readLine();
		int bl = bomb.length();
		ArrayList<Character> st = new ArrayList<Character>();
		for(int i = 0; i < tmp.length; i++) {
			st.add(tmp[i]);
			int size = st.size();
			if (size>=bl) {
				boolean bom = true;
				for(int j = bl-1; j>=0; j--) {
					if(st.get(j+size-bl) != bomb.charAt(j)) {
						bom = false;
						break;
					}
				}
				if(bom){
					for(int j = 0; j < bl; j++)
						st.remove(st.size()-1);
				}
			}
		}
		if(st.size()==0)
			System.out.println("FRULA");
		else
			System.out.println(st.stream().map(e->e.toString()).collect(Collectors.joining()));
	}
}