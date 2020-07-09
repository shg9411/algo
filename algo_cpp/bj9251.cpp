#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int dp[1001][1001];
char a[1001], b[1001];

int main(void)
{
	scanf("%s", a);
	scanf("%s", b);
	int aLen, bLen;
	aLen = strlen(a);
	bLen = strlen(b);

	for (int i = 1; i <= aLen; i++)
	{
		for (int j = 1; j <= bLen; j++)
		{
			if (a[i - 1] == b[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
			else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
		}
	}
	printf("%d", dp[aLen][bLen]);
	return 0;
}