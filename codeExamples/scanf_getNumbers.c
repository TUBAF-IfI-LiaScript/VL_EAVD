#include <stdio.h>

int main(){
  int i;
	float a;
	char b;
	printf("Bitte folgende Werte eingeben %%c %%f %%d: ");
	scanf(" %c %f %d", &b, &a, &i);
	printf("%c %f %d\n", b, a, i);
	return 0;
}
