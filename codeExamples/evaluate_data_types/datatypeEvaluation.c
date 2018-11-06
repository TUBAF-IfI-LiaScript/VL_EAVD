#include <stdio.h>
#include <stdint.h>

int main()
{
  <type> x;
  
  x= 1;
  
  unsigned long i;

  //ulong max == 4294967295
  for (i=0; i<1000000000; i++){
    if (x>=0x0FFF){
        x=1;
    }
    x=x*52;
    //x=x+0x100;
    //x=x<<1;
  }
  printf("%lu\n", (unsigned long)x);
  return 0;
}