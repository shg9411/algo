#include <cstdio>
using namespace std;


int main(void) {
	long long x, y, z, l,r,mid,tmp,ans = 0;
	while(~scanf("%lld %lld",&x,&y)){
	z = y*100 / x;
	if (z >= 99) {
		printf("-1\n");
		return 0;
	}
	l = 0;
	r = x;
	while (l <= r) {
		mid = (l + r) / 2;
		tmp = (y + mid) * 100 / (x + mid);
		if (tmp > z) 
			r = mid- 1;
		else{
            ans=mid+1;
			l = mid+ 1;
        }
	}
	printf("%d\n",ans);
    }
	return 0;
}