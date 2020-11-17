## `void`-Zeiger

`void`-Zeiger ist zu jedem anderen Daten-Zeiger kompatibel und wird
verwendet, wenn der Datentyp des Zeigers noch nicht feststeht.
In C ist die implizite und explizite Typumwandlung des `void`-Zeigers in einen anderen Typ möglich.

```c
int a=5;
void *pv=&a;
int *pi=pv;
int *pii=(int*)pv;
```
Vorwiegend findet ein `void`-Zeiger Anwendung in Funktionen, die mit
unterschiedlichen Zeigern aufgerufen werden bzw. unterschiedliche Zeiger
als einen Rückgabewert liefern.

Beispiele:
* Die Funktion `memcmp()` (`<string.h>`) zum Vergleichen von Zeichenketten erlaubt die Verwendung mit `char*` und `int*`.
* Das Ergebnis der Funktion `malloc()` (`<stdlib.h>`) zum Bereistellen des Speicherplatzes kann in `char*`, `int*`, `double*` usw. umgewandelt werden.

```c
int memcmp (const void*, const void*, size_t);
void *malloc(size_t size);
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
   char str1[]="abcde";
   char str2[]="ABCDE";

   if(memcmp(str1,str2, sizeof(str1)) == 0)
      printf("Strings sind gleich\n");
   else
      printf("Strings sind nicht gleich\n");

   return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)
