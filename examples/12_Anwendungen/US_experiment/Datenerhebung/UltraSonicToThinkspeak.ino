#include "Sensor.h"
#include "ThingSpeakTUBAF.h"

DevI2C *ext_i2c;
HTS221Sensor *ht_sensor;
RGB_LED rgbLed;

char apiKey[] = "MySecretKey";  // Muss mit Ihrem Eintrag ersetzt werden.

const int trigPin = 16;
const int echoPin = 5;

void initWeatherSensor() {
  ext_i2c = new DevI2C(D14, D15);
  ht_sensor = new HTS221Sensor(*ext_i2c);
  ht_sensor->init(NULL);
}

void initDistanceSensor(){
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);  // Sets the echoPin as an Input
}

float getTempData() {
  float temperature;
  ht_sensor->enable();
  ht_sensor->getTemperature(&temperature);
  ht_sensor->disable();
  ht_sensor->reset();

  char buff[16];
  sprintf(buff, "Temp:%sC\r\n", f2s(temperature, 1));
  Screen.print(1, buff);

  return temperature;
}

float getHumData() {
  float humidity;
  ht_sensor->enable();
  ht_sensor->getHumidity(&humidity);
  ht_sensor->disable();
  ht_sensor->reset();

  return humidity;
}

float calcDist(long duration, float temp){
  float us_speed = (331.3 + (0.606 * temp)) / 1000 / 1000 * 100;
  return us_speed * duration / 2;
}

float getDistData() {

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  while(digitalRead(echoPin) == LOW);
  long int start = micros();
  while(digitalRead(echoPin) == HIGH);

  float duration = micros()-start;
  char buff[16];
  sprintf(buff, "Dist:%scm\r\n", f2s(calcDist(duration, 25), 1));
  Screen.print(2, buff);

  return duration;
}

void setup() {
  Serial.begin(115200);
  initWeatherSensor();
  initDistanceSensor();
  InitWiFi();
}

void loop() {
  float dataForUpload[] = {getTempData(),
                           getHumData(),
                           getDistData()};

  int n_dataForUpload = sizeof(dataForUpload)/sizeof(dataForUpload[0]);
  if(hasWifi)
  {
    Screen.print(0, "Connected");
    updateThingSpeak(apiKey, dataForUpload, n_dataForUpload);
  }
  else Screen.print(0, "Not connected");
  delay(20*1000);
  Screen.clean();
}