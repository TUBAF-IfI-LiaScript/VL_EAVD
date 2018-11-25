#include <stdio.h>
#include <string.h>

#define ENTRIES 3

int main() {

  enum {Jan, Feb, Maerz, April, Mai, Juni, Juli, Aug, Sept, Okt, Nov, Dez};

  char months[12][20] = {"Januar", "Februar", "Maerz", "April",
                         "Mai", "Juni", "Juli", "August", "September",
                         "Oktober", "November", "Dezember"};

  struct datum
  {
      unsigned char tag;     // wert < 31
      unsigned char monat;   // wert < 12
      short jahr;            // wert < 2048
  };

  struct datum geburtstage [ENTRIES] = {{18, April, 1986},
                                        {12, Mai, 1820}};

  geburtstage[2].tag = 5;
  geburtstage[2].monat = Sept;
  geburtstage[2].jahr = 1905;

  for (int i=0; i<ENTRIES; i++)
    printf("%2d. %-10s %4d\n", geburtstage[i].tag,
                               months[geburtstage[i].monat],
                               geburtstage[i].jahr);

  return 0;
}
