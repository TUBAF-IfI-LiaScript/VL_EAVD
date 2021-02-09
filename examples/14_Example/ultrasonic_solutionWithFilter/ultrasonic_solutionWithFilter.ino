#include "HTS221Sensor.h"

#define MAGICLIMIT 10

const int trigPin = 16;
const int echoPin = 5;

long int start = 0;
float distance = 15;
float oldDistance = 0;
int valid = 50;

DevI2C ext_i2c(D14,D15);
HTS221Sensor sensor(ext_i2c);
float temperature = 0;

float calcDist(long duration, float temp){
  float us_speed = (331.3 + (0.606 * temp)) / 1000 / 1000 * 100;
  return us_speed * duration / 2;
}

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);

  sensor.init(NULL);
  sensor.enable();
}

void loop() {

  sensor.getTemperature(&temperature);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  while(digitalRead(echoPin) == LOW);
  start = micros();
  while(digitalRead(echoPin) == HIGH);

  distance = calcDist(micros()-start, temperature);
  if (abs(oldDistance - distance) < MAGICLIMIT) valid = 50;
  else valid = 0;
  
  Serial.print("distance:");
  Serial.println(distance, 2);
  //Serial.print(" valid:");
  //Serial.println(valid);
  //oldDistance = distance;
  delay(50);
}
