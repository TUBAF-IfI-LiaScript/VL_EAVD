#include "RGB_LED.h"
RGB_LED rgbLed;

long myTimer = 0;
long myTimeout = 1000;

void alarm(){
  rgbLed.setColor(255, 0, 0);
}

void setup() {
  attachInterrupt(USER_BUTTON_B, alarm, FALLING);
  Serial.begin(9600);
}

void loop() {
  rgbLed.setColor(0, 255, 255);
  Serial.println("Ich rechne ganz fleißig vor mich hin!");
  delay(2000);
}
