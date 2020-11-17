#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a = 5;
  float b = 3.2342;
  int * ptr_a;
  ptr_a = a;
  printf("Pointer ptr_a                  %p\n", ptr_a);
  printf("Wert hinter dem Pointer ptr_a  %d\n", *ptr_a);
  return EXIT_SUCCESS;
}
