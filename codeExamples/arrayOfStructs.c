#include <stdio.h>
#include <string.h>

#define ENTRIES 3

int main() {
  struct datum
  {
      int tag;
      char monat[10];
      int jahr;
  };

  struct datum geburtstage [ENTRIES] = {{18, "April", 1986},
                                        {12, "Februar", 1820}};

  // Ergänzen Sie Einträge für den letzten Datensatz!
  // ...

  for (int i=0; i<ENTRIES; i++)
    printf("%2d. %-10s %4d\n", geburtstage[i].tag,geburtstage[i].monat,geburtstage[i].jahr);

  return 0;
}
