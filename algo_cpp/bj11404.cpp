#include <iostream>
using namespace std;


int main(void){
    cin.tie(0);cout.tie(0);
    ios_base::sync_with_stdio(0);
    int n,m;
    cin >> n >> m;
    int arr[n][n];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i-j)
                arr[i][j] = 987654321;
            else
                arr[i][j] = 0;
        }
    }
    
    for(int i = 0; i < m; i++){
        int s,e,c;
        cin >> s >> e >> c;
        if(c<arr[s-1][e-1])
            arr[s-1][e-1] = c;
    }
        
    for(int k = 0; k < n; k++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(arr[i][k]+arr[k][j]<arr[i][j])
                    arr[i][j] = arr[i][k]+arr[k][j];
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(arr[i][j]<987654321)
            	cout<< arr[i][j] <<' ';
            else 
            	cout<<"0 ";
        }
        cout<<'\n';
    }
    return 0;
}