#include <iostream>
using namespace std;

int main(void) {
    cin.tie(0); ios_base::sync_with_stdio(0);
    long long int n, tmp;
    cin >> n;
    tmp = n;
    for (long long int i = 2; i * i <= n; i++) {
        if (n % i != 0)
            continue;
        while (n % i == 0)
            n /= i;
        tmp /= i;
        tmp *= (i - 1);
    }
    if (n != 1)
        tmp = tmp / n * (n - 1);
    cout << tmp;
    return 0;
}