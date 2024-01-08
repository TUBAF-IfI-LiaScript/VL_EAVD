#include <iostream>
#include <cmath>
using namespace std;

void runden(float* a){
    if (*a < 0)
       *a = (int)(*a - 0.5);
    else
       *a = (int)(*a + 0.5);
}

int main(void) {
  float value = -8.4565;
  float *pointer = &value;
  runden(pointer);
  cout<<"Eingabewert "<<value<<" - Ausgabewert "<<*pointer<<"\n";
  return 0;
}