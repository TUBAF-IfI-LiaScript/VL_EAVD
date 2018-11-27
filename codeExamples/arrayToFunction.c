#include <stdio.h>
#include <string.h>

struct datensatz{
  char name[20];
  int alter;
  int note;
};

// Definitionsteil
struct datensatz initDatensatz(char name[], int alter, int note){
   struct datensatz student;
   strcpy(student.name, name);
   student.alter = alter;
   student.note = note;
   return student;
}

int main() {
   struct datensatz eintrag = initDatensatz("Micky Maus", 50, 1);
   printf("Name %s \nAlter %d \nNote %d\n", eintrag.name, eintrag.alter, eintrag.note);
   return 0;
}
