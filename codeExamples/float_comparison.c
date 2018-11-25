#include <stdio.h>

int main() {
  int a[] = {5, 2, 2, 5, 6};   // Alternative Form der Initialisierung
  float b[5] = {1.0, [4]=6.4};
  for (int i=0; i<5; i++){
    printf("%d  %f\n", a[i], b[i]);
  }
  return 0;
}
