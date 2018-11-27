#include <stdio.h>
#include <math.h>

void Info(){
    printf("Dieses Programm rundet Zahlenwerte.\n");
    printf("-----------------------------------\n");
}

int runden(float a){
    if ((a - (int)a)<0.5)
       return ((int) a);
    else
       return (((int) a) + 1);
}

float rundenf(float a, int nachkomma){
    float shifted= a* pow(10, nachkomma);
    if ((shifted - (int)shifted)<0.5)
       return ((float)(int)shifted * pow(10, -nachkomma));
    else
       return ((float)((int)shifted + 1) * pow(10, -nachkomma));
    printf("%f", shifted);
}

int main(){
    Info();
    float input = 8.4535;
    printf("Eingabewert %f - Ausgabewert %d\n", input, runden(input));
    printf("Eingabewert %f - Ausgabewert %f\n", input, rundenf(input,2));
}
