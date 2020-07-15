#include<cstdio>
using namespace std;

bool alpha[26];
bool ans[26];
int l, c;

void dfs(int idx, int cnt) {
	if (cnt == l) {
		int mo = 0;
		if (ans['a' - 'a'])
			mo++;
		if (ans['e' - 'a'])
			mo++;
		if (ans['i' - 'a'])
			mo++;
		if (ans['o' - 'a'])
			mo++;
		if (ans['u' - 'a'])
			mo++;
		if (mo && cnt - mo > 1) {
			for (int i = 0; i < 26; i++) {
				if (ans[i])
					printf("%c", i + 'a');
			}
			printf("\n");
		}
		return;
	}
	for (int i = idx; i < 26; i++) {
		if (alpha[i]) {
			ans[i] = 1;
			dfs(i + 1, cnt + 1);
			ans[i] = 0;
		}
	}
}

int main(void)
{
	char tmp;
	scanf("%d%d\n", &l, &c);
	while (c--) {
		tmp = (char)getchar();
		getchar();
		alpha[tmp - 'a'] = 1;
	}
	dfs(0, 0);
	return 0;
}