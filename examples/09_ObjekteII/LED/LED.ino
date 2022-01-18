#include "RGB_LED.h"

PinName red = PB_4;
PinName green = PB_3;
PinName blue = PC_7;

RGB_LED rgbLed(red, green, blue);

uint8_t color[][3] = {
        {255, 0, 0},                // red
        {0, 255, 0},                // green
        {0, 0, 255},                // blue
        {0, 0, 0},                  
        {255, 255, 0},
        {0, 255, 255},
        {255, 0, 255},
        {255, 255, 255}
    };

void setup(){
}

void loop(){
   for(int i = 0; i< 8; ++i)
   {
       Serial.printf("Red: %d, Green: %d, Blue: %d\n", color[i][0], color[i][1], color[i][2]);
       rgbLed.setColor(color[i][0], color[i][1], color[i][2]);
       delay(1000);
   }
   Serial.println("Turn off");
   rgbLed.turnOff();
   delay(1000);
}
