#include <iostream>
#include <cstring>
using namespace std;

char str[1000020], bomb[40];
int len, blen, tmp = 0;
bool ok;

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	cin >> str >> bomb;
	len = strlen(str);
	blen = strlen(bomb);
	for (int i = 0; i < len; i++) {
		str[tmp] = str[i];
		if (tmp >= blen - 1 && str[tmp] == bomb[blen - 1]) {
			ok = true;
			for (int j = 1; j < blen; j++) {
				if (str[tmp - j] != bomb[blen - 1 - j]) {
					ok = false;
					break;
				}
			}
			if (ok)
				tmp -= blen;
		}
		tmp++;
	}
	if (tmp > 0) {
		for (int i = 0; i < tmp; i++)
			cout << str[i];
	}
	else
		cout << "FRULA";
	return 0;
}