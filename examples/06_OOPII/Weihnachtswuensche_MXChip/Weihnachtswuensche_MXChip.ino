#include <OledDisplay.h>

void setup(){
    Screen.init();
}
void loop(){
    // print a string to the screen with wrapped = true
    Screen.print("Hohoho\nEin froehliches\nWeihnachtsfest\n2023 !!!", true);
    delay(2000);
    Screen.clean();
    delay(1000);
}
