#include <stdio.h>
#include <math.h>

void Info(void){
    printf("Dieses Programm rundet Zahlenwerte.\n");
    printf("-----------------------------------\n");
}

int runden(float a){
    if ((a - (int)a)<0.5)
       return ((int) a);
    else
       return (((int) a) + 1);
}

double rundenf(float a, int nachkomma){
    // rundet float werte an durch nachkomma spezifizierten Stellen
    // rundenf(3610, 2) ->  3600
    // rundenf(3680, 2) ->  3700
    // rundenf(3680.234, -2) ->  3700.240000
    return 0;
}

int main(){
    Info();
    float input = 3662.6535;
    int result =  runden(input);
    printf("Eingabewert %f - Ausgabewert %d\n", input, result);
    printf("Eingabewert %f - Ausgabewert %f\n", input, rundenf(input, 2));
}


// Lösung
// ---------------------------------------------------
// double shifted= a * pow(10, -nachkomma);
// if ((shifted - (int)shifted)<0.5)
//    return (int)shifted * pow(10, nachkomma);
// else
//    return ((int)shifted + 1) * pow(10, nachkomma);
