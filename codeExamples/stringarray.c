#include <stdio.h>

int main() {
  printf("Diese Form eines Strings haben wir bereits mehrfach benutzt!\n");
  // Alternativ
  char a[50];
  printf("->%s<-\n", a);
  const char b[] = { 'H', 'a', 'l', 'l', 'o', ' ',
                     'F', 'r', 'e', 'i', 'b', 'e', 'r', 'g'};
  printf("->%s<-\n", b);
  const char c[] = {"Noch eine \0Moeglichkeit"};
  printf("->%s<-\n", c);
  char d[] = { 80, 114, 111, 122, 80, 114, 111, 103, 32, 50, 48, 49, 56  };
  printf("->%s<-\n", d);
  return 0;
}
