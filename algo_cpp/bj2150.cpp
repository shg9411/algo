#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> adj[10001];
vector<int> stack;
vector<vector<int>> ans;
int dfsn[10001],sccn[10001];
bool finished[10001];
int sn = 0, cnt = 0;

int dfs(int u){
    dfsn[u] = ++cnt;
    stack.push_back(u);
    
    int res = dfsn[u];
    for(auto v : adj[u]){
        if(dfsn[v]==0){
            int tmp = dfs(v);
            res = res<tmp?res:tmp;
        }else if(!finished[v]){
            res = res<dfsn[v]?res:dfsn[v];
        }
    }
    if(res==dfsn[u]){
        vector<int> tmpScc;
        while(1){
            int tmp = stack.back();stack.pop_back();
            tmpScc.push_back(tmp);
            finished[tmp] = 1;
            sccn[tmp] = sn;
            if(tmp==u)
              break;
        }
        sort(tmpScc.begin(),tmpScc.end());
        ans.push_back(tmpScc);
        sn++;
    }
    return res;
}

int main(void){
    int v,e;
    
    scanf("%d %d",&v,&e);
    for(int i = 0; i < e; i++){
        int u,v;
        scanf("%d %d",&u,&v);
        adj[u].push_back(v);
    }
    for(int i = 1; i <= v; i++){
        if(dfsn[i]==0)
            dfs(i);
    }
    
    sort(ans.begin(),ans.end());
    printf("%d\n",sn);
    for(auto scc : ans){
        for(auto tmp : scc)
            printf("%d ",tmp);
        printf("-1\n");
    }
    return 0;
}