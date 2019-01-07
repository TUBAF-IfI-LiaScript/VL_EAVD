#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define FILENAME "./data/baby-names.csv"
#define INITIALSIZE 100
#define STEPWIDTH 20

unsigned int max_datensaetze = INITIALSIZE;

struct datensatz{
  unsigned int year;
  char name[24];
  char girlsname;
};

int main(int argc, char *argv[])
{
  FILE *in = fopen(FILENAME,"r");
  if(in==NULL){
    perror("File open error");
    exit(EXIT_FAILURE);
  }

  struct datensatz * names;
  names = malloc(max_datensaetze * sizeof(*names));

  unsigned int year;
  int count = 0;
  char name[24];
  float prob;
  char sex[7];
  char not_found = 0;
  do{
    if (fscanf(in,"%d,%[^,],%f,%s", &year, name, &prob, sex) == 4) {
      if (0 == strcmp(sex, "\"boy\"")){
        // neuer Name?
        not_found = 1;
        for (int i=0; i<count; i++){
          if (0 == strcmp(names[i].name, name)) {
            not_found = 0;
            break;
          }
        }
        if (not_found){
          // Hinreichend Speicher im array?
          if (count >= max_datensaetze){
            max_datensaetze += STEPWIDTH;
            names = realloc(names, max_datensaetze * sizeof(*names));
          }
          strcpy(names[count].name, name);
          count++;
        }
      }else{
        for (int i=0; i<count; i++){
          if (0 == strcmp(names[i].name, name)) {
            names[i].girlsname = 1;

            break;
          }
        }
      }
    }
  } while (!feof(in));

  for (int i=0; i<count; i++){
    if (1 == names[i].girlsname){
      printf("%s ", names[i].name);
    }
  }
  free(names);
  fclose(in);
  return 0;
}
