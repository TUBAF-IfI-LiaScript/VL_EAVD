/* Beispiel aus dem Lehrbuch des Rheinwerk-Verlages "C von A bis Z"
   Jürgen Wolf, 2017
   penbook.rheinwerk-verlag.de/c_von_a_bis_z/013_c_kommandozeilenargumente_001.htm
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
   int i, j ;
   long y, erg;

   if(argc < 4) {
      printf("Benötige mindestens 4 Argumente!\n");
      printf("Aufruf: %s <zahl><op><zahl> ...\n", *argv);
      return EXIT_FAILURE;
   }
   /* 1.Zahl in einen Integer konvertieren*/
   erg = strtol(argv[1], NULL, 10);
   if( erg == 0 ) {
      printf("Keine gültige Ganzzahl ... \n");
      return EXIT_FAILURE;
   }

   for(i = 1; i < argc-1; i += 2) {
      for(j=i+1; j < i+2; j++) {
         y = strtol(argv[i+2], NULL, 10);
         if( y == 0 ) {
            printf("Keine gültige Ganzzahl ... \n");
            printf("argc: %d (%s)?!\n", i+2, argv[i+2]);
            return EXIT_FAILURE;
         }
         if(strcmp(argv[j],"+") == 0)
            erg += y;
         else if(strcmp(argv[j],"-") == 0)
            erg -= y;
          else if(strcmp(argv[j], "x") == 0)
             erg *= y;
          else if(strcmp(argv[j],"/") == 0)
             erg/=y;
          else {
             printf("Ungültiger Operand: %s\n", argv[j]);
             return EXIT_FAILURE;
          }
      }
   }
   printf("%ld\n",erg);
   return EXIT_SUCCESS;
}
