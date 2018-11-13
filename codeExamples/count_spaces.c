#include <stdio.h>

int main(){
  int c;
  int zaehler = 0;
  printf("Leerzeichenzähler - zum Beenden \"_\" [Enter]\n");
  while((c = getchar()) != '_')
  {
    if(c == ' ')
      zaehler++;
  }
  printf("Anzahl der Leerzeichen: %d\n", zaehler);
  return 0;
}
