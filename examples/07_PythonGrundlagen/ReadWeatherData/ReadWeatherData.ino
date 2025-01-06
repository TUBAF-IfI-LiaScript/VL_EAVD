
#include <Arduino_HS300x.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!HS300x.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }
}

void loop() {
  // read all the sensor values
  float temperature = HS300x.readTemperature();
  float humidity    = HS300x.readHumidity();

  // print each of the sensor values
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.println();
  delay(100);
}