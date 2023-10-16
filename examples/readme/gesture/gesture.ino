/*
This program was motivated by arduino docs
https://docs.arduino.cc/tutorials/nano-33-ble-sense/gesture-sensor
Thanks for sharing!
*/

#include <Arduino_APDS9960.h>

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT); 
  while (!Serial);
  if (!APDS.begin()) {
    Serial.println("Error initializing APDS9960 sensor!");
  }
}

void loop() {
  if (APDS.gestureAvailable()) {
    int gesture = APDS.readGesture();
    Serial.println(gesture);
    if (gesture == GESTURE_LEFT)
    {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);
        digitalWrite(LED_BUILTIN, LOW);
    }
  }
}