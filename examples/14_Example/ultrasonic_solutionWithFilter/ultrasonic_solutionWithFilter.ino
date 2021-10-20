#include "HTS221Sensor.h"
#define WINDOW_SIZE 8

int id = 0;
float value = 0;
float sum = 0;
float samples[WINDOW_SIZE];
float mean = 0;

const int trigPin = 16;
const int echoPin = 5;

long int start = 0;
float distance = 0;

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

  sum = sum - samples[id];       // Remove the oldest entry from the sum
  samples[id] = distance;           // Add the newest reading to the window
  sum = sum + distance;                // Add the newest reading to the sum
  id = (id+1) % WINDOW_SIZE;  // Increment the index, and wrap to 0 if it exceeds the window size

  mean = sum / WINDOW_SIZE;         // Divide the sum of the window by the window size for the result
  
  Serial.print("raw:");
  Serial.print(distance,2);
  Serial.print(" mean:");
  Serial.println(mean,2);

  // Zustandsautomat für die Messung der Amplitude 
 
  delay(50);
}
