package DP;

import java.util.ArrayList;

public class Main {
	
	static void dfs(ArrayList<Integer> ar, int x, int y) {
		if(x==3&&y==4) {
			for(int i : ar) {
				System.out.print(i+" ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		ArrayList<Integer> ar = new ArrayList<Integer>();
		ar.add(0);
		ar.add(3);
		ar.remove(ar.size()-1);
		int[] i = {3,4};
		System.out.println(i.length);
		dfs(ar,3,4);
	}
}
