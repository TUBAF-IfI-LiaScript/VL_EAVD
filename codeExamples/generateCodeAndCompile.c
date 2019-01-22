#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char programmCode[] = "#include <stdio.h> \n int main(){printf(\"C-Code Datei generiert und kompiliert!\"); return 0;}";

int main(void) {
  printf("Schreibe den Code in Datei ...\n");
  FILE * fp;
  fp = fopen ("myCode.c","w");
  fprintf (fp, programmCode);
  fclose (fp);

  char command[50];
  printf("Kompiliere ...\n");
  strcpy(command, "gcc myCode.c -o myCode.out" );
  system(command);
  printf("Führe aus ...\n");
  strcpy(command, "./myCode.out" );
  system(command);
  return EXIT_SUCCESS;
}
