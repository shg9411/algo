import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q1012 {
   static int n, m, k, T, count = 0;
   static int[][] arr;
   static int dx[] = { -1, 0, 1, 0 };
   static int dy[] = { 0, -1, 0, 1 };

   public static void main(String[] args) throws IOException {
      // TODO Auto-generated method stub
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      T = Integer.parseInt(st.nextToken());
      for (int t = 0; t < T; t++) {
         st = new StringTokenizer(br.readLine());
         m = Integer.parseInt(st.nextToken());
         n = Integer.parseInt(st.nextToken());
         k = Integer.parseInt(st.nextToken());
         arr = new int[n][m];

         for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[y][x] = 1;
         }
         for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
               if (arr[i][j] == 1) {
                  DFS(i, j);
                  count++;
               }
            }
         }
         System.out.println(count);
         count = 0;
      }
   }

   public static void DFS(int x, int y) {

      for (int i = 0; i < 4; i++) {
         int nextX = x + dx[i];
         int nextY = y + dy[i];

         if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
            continue;
         }
         if (arr[nextX][nextY] == 0) {
            continue;
         }
         arr[nextX][nextY] = 0;
         DFS(nextX, nextY);
      }
   }

}