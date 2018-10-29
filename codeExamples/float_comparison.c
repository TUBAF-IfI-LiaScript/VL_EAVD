#include<stdio.h>
#include<float.h>

int main() {
	printf("float Genauigkeit :%d \n", FLT_DIG);
	printf("double Genauigkeit :%d \n", DBL_DIG);
	float x = 0.1;
  if (x == 0.1) {
    printf("Gleich\n");
  }else{
    printf("Ungleich\n");
  }
  return 0;
}
