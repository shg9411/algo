package DP;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			String[] personA = new String[n];
			String[] personB = new String[m];
			ArrayList<String> result = new ArrayList<String>();
			for(int i=0;i<personA.length;i++) {
				personA[i] = br.readLine();
			}
			for(int i=0;i<personB.length;i++) {
				personB[i] = br.readLine();
			}
			Arrays.sort(personA);
			Arrays.sort(personB);
			int length = (personA.length < personB.length) ? personA.length : personB.length;
			for(int i=0;i<length;i++) {
				int index = 0;
				if(personA.length < personB.length) {
					index = binarySearch(personB, personA[i], 0 , personB.length);
					if(index != -1) result.add(personB[index]);
				}else {
					index = binarySearch(personA, personB[i], 0 , personA.length);
					if(index != -1) result.add(personA[index]);
				}
			}
			System.out.println(result.size());
			for(int i=0;i<result.size();i++) {
				System.out.println(result.get(i));
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	private static int binarySearch(String[] temp, String target, int low, int high) {
		if(low > high) return -1;
		int mid = (low + high) / 2;
		if(temp[mid].equals(target)) { 
			return mid;
		}else if ((int)temp[mid].toCharArray()[0] > (int)target.toCharArray()[0]) { 
			return binarySearch(temp, target, low, mid-1);
		}else {
			return binarySearch(temp, target, mid+1, high);
		}
	}
}
