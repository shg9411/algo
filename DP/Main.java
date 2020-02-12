package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
class XY{
    int x,y;
    XY(int x, int y){
        this.x=x;
        this.y=y;
    }
}
public class Main {
	static int[] dx= {-1,0,1,0};
	static int[] dy= {0,1,0,-1};
	static int[][] map;
	static int[][] ans;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int cnt=1;
		int t=Integer.parseInt(br.readLine());
		while(t!=0) {
			map=new int[t+1][t+1];
			ans=new int[t+1][t+1];
			for(int i=1; i<=t; i++) {
				st=new StringTokenizer(br.readLine());
				for(int j=1; j<=t; j++) {
					map[i][j]=Integer.parseInt(st.nextToken());
				}
			}
			ans[1][1]=map[1][1];
			Queue<XY> q=new LinkedList<>();
			q.add(new XY(1,1));
			while(!q.isEmpty()) {
				XY xy=q.poll();
				for(int i=0; i<4; i++) {
					int nx=xy.x+dx[i];
					int ny=xy.y+dy[i];
					if(nx<1 || ny<1 || nx>t || ny>t) 
						continue;
					if(ans[nx][ny]!=0) {
						if(ans[nx][ny]>ans[xy.x][xy.y]+map[nx][ny]) {
							ans[nx][ny]=ans[xy.x][xy.y]+map[nx][ny];
							q.add(new XY(nx,ny));
						}
					}
					else if(ans[nx][ny]==0) {
						ans[nx][ny]=map[nx][ny]+ans[xy.x][xy.y];
						q.add(new XY(nx,ny));
					}
				}
			}
			System.out.println("Problem "+(cnt++)+": "+ans[t][t]);
			t=Integer.parseInt(br.readLine());
		}


	}

}