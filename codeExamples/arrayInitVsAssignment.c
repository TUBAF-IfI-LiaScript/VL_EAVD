#include <stdio.h>
#include <string.h>

int main() {
  char a[] = "Das ist der orginal Text";
  //a = "Das ist ein neuer Text";  // Compiler Error
  strcpy(a, "Das ist ein neuer Text");
  a[0]='X';
  printf("%s\n",a);
  return 0;
}
