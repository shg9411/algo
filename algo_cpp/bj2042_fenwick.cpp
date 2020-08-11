#include<cstdio>
using namespace std;
inline void scan(int& x)
{
	int c = getchar_unlocked();
	x = 0;
	int neg = 0;
	for (; ((c < 48 || c>57) && c != '-'); c = getchar_unlocked());
	if (c == '-') {
		neg = 1;
		c = getchar_unlocked();
	}
	for (; c > 47 && c < 58; c = getchar_unlocked()) {
		x = (x << 1) + (x << 3) + c - 48;
	}
	if (neg)
		x = -x;
}

int n, m, k, tree[1000001];
long long fenwick[1000001];

void update(int i, int val){
    while(i<=n){
        fenwick[i] += val;
        i+=(i&-i);
    }
}

long long sum(int i){
    long long res = 0;
    while(i>0){
        res+=fenwick[i];
        i-=(i&-i);
    }
    return res;
}

int main(void)
{	
	scan(n);scan(m);scan(k);
	for (int i = 1; i <= n; i++){
		scan(tree[i]);
        update(i,tree[i]);
    }
    for(int i = 0; i < m+k; i++){
        int a,b,c;
        scan(a);scan(b);scan(c);
        if(a==1){
            int diff = c-tree[b];
            update(b,diff);
            tree[b] = c;
        }else
            printf("%lld\n",sum(c)-sum(b-1));
    }

	return 0;
}