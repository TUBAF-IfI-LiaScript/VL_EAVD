#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void showHelp(){
  printf("Anwendung des Programms: \n");
  printf("writeTextFile -f=filename -i=text\n");
}

int write2File(const char *filename, const char *text){
  FILE *f = fopen(filename, "w");
  if (f == NULL)
  {
      printf("Error opening file!\n");
      return -1;
  }
  int count = fprintf(f, "%s\n", text);
  fclose(f);
  return count;
}

int main( int argc, char *argv[] )  {
  char filename[30];
  char text[100];
  if( argc != 3 ) {
    printf("False Parameter Anzahl!.\n");
    showHelp();
    return EXIT_FAILURE;
  }
  else {
    printf("Korrekte Parameteranzahl!\n");
    if (!strncmp(argv[1], "-f=", 3)){
      strcpy(filename, argv[1] + 3);
    }
    if (!strncmp(argv[2], "-f=", 3)){
      strcpy(filename, argv[2] + 3);
    }
    if (!strncmp(argv[1], "-i=", 3)){
      strcpy(text, argv[1] + 3);
    }
    if (!strncmp(argv[2], "-i=", 3)){
      strcpy(text, argv[2] + 3);
    }
    printf("%s -> %s\n", text, filename);
    //write2File("text.txt", "Hossa!");
    write2File(filename, text);
    return EXIT_SUCCESS;
  }
}
