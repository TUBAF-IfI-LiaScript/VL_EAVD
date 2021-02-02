#include "RGB_LED.h"
RGB_LED rgbLed;

volatile unsigned long start;
const int period = 2000;

void alarm(){
  start = millis();
}

void setup() {
  attachInterrupt(USER_BUTTON_B, alarm, FALLING);
  Serial.begin(9600);
}

void loop() {
  if (millis() < start + period) rgbLed.setColor(255, 0, 0);
  else rgbLed.setColor(0, 255, 255);
}
