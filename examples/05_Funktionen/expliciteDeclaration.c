#include <stdio.h>
#include "main.h"

int main(void) {
  int i = foo();       // <- Aufruf der Funktion
  printf("i=%d\n", i);
  return 0;
}

int foo(void){         // <- Definition der Funktion
  return 3;
}
