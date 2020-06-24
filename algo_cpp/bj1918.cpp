#include <cstdio>
#include <cstring>

int pri(char c) {
	if (c == '(')
		return 0;
	if (c == '+' or c == '-')
		return 1;
	return 2;
}
int main(void) {
	char exp[101], res[101], stack[101], tmp;
	int j,top = -1, rtop = -1;

	scanf("%s", exp);
	for (int i = 0; exp[i]!='\0'; i++) {
		tmp = exp[i];
		if (tmp == '(')
			stack[++top] = tmp;
		else if (tmp == ')') {
			for (j = top; stack[j] != '('; j--)
				res[++rtop] = stack[j];
			top = --j;
		}
		else if (tmp >= 'A' && tmp <= 'Z')
			res[++rtop] = tmp;
		else {
			for (j = top; j >= 0 && pri(stack[j]) >= pri(tmp); j--)
				res[++rtop] = stack[j];
			top = j;
			stack[++top] = tmp;
		}
	}
	for (j = top; j > -1; j--)
		res[++rtop] = stack[j];
	//res[++rtop] = '\0';
	//printf("%s", res);
	for (int x = 0; x <= rtop; x++)
		printf("%c", res[x]);

	return 0;
}