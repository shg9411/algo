package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test {
   static int n, count = 0;
   static int arr[];

   public static void main(String[] args) throws IOException {
      // TODO Auto-generated method stub
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      arr = new int[n];
      int max = 0;
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; i++)
         arr[i] = Integer.parseInt(st.nextToken());
      int index;
      int tmp2 = 0;
      for (int i = 0; i < n; i++) {
         int tmp = arr[i];
         index = i;
         for (int j = i; j < n; j++) {
            if (arr[j] >= tmp) {
               count++;
               tmp = arr[j];
               tmp2 = index;
               index = j;
            } else if (arr[tmp2] <= arr[j] && tmp >= arr[tmp2]) {
               tmp = arr[j];
               tmp2 = index;
               index = j;
            } else
               continue;
         }
         max = Math.max(max, count);
         count = 0;
      }
      System.out.println(max);
   }

}