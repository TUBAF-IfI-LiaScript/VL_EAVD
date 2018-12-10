// Read baby names from US
// the file is available in the project folder /data

#include <stdio.h>
#include <stdlib.h>
#define FILENAME "./data/baby-names.csv"

int main(int argc, char *argv[])
{
  FILE *in = fopen(FILENAME,"r");
  if(in==NULL){
    perror("File open error");
    exit(EXIT_FAILURE);
  }

  unsigned int year, year_old = 0;
  int count = 0;
  char name[24];
  float prob;
  char sex[6];
  while(1){
    if( feof(in) ) {break;}
    count ++;
    fscanf(in,"%d,%[^,],%f,%s", &year, name, &prob, sex);
    if (year != year_old){
      if (year%10==0) {
        printf("%d,%10s,%1.4f,%s\n", year, name, prob, sex);
      }
      year_old = year;
    }
  }
  printf("\n%d Datensätze gelesen\n", count);
  fclose(in);
  return 0;
}
