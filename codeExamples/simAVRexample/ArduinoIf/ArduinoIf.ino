const int SensorPin = A0;
int sensorValue = 0;


void setup() {
  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);

  pinMode(SensorPin, INPUT);
}

void loop() {
  sensorValue = analogRead(SensorPin);
  if (sensorValue > 125) digitalWrite(0, HIGH);
  else digitalWrite(0, LOW);
  if (sensorValue > 250) digitalWrite(1, HIGH);
  else digitalWrite(1, LOW);
  if (sensorValue > 375) digitalWrite(2, HIGH);
  else digitalWrite(2, LOW);
  if (sensorValue > 500) digitalWrite(3, HIGH);
  else digitalWrite(3, LOW);
  if (sensorValue > 625) digitalWrite(4, HIGH);
  else digitalWrite(4, LOW);
  if (sensorValue > 750) digitalWrite(5, HIGH);
  else digitalWrite(5, LOW);
  if (sensorValue > 875) digitalWrite(6, HIGH);
  else digitalWrite(6, LOW);
  if (sensorValue > 1000) digitalWrite(7, HIGH);
  else digitalWrite(7, LOW);
}