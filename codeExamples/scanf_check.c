#include <stdio.h>

int main(){
  char str[10];
	printf("Bitte Zahlen eingeben!");
	if (scanf("%9[0-9]", str) != 1){
		printf("Nur Zahlen!\n");
		return 1;
	}
	printf("Gueltiger Wert %s\n", str);
	return 0;
}

//%[^0-9]   //keine Zahlen
//%[A-Z]    //alle Großbuchstaben von A bis Z
//%[a-z]    //alle Kleinbuchstaben von a bis z
//Alle Groß- und Kleinbuchstaben von A bis F (Hexadezimalzahlen)
//%[a-fA-F]
