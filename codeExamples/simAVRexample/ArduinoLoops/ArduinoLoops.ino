const int SensorPin = A0;
int sensorValue = 0;

void setup() {
  for (int i = 0; i<=7; i++){
  	pinMode(i, OUTPUT);
  }
  pinMode(SensorPin, INPUT);
}

void loop() {
  sensorValue = analogRead(SensorPin);
  for (int i = 0; i<=7; i++){ 
    if (sensorValue > (i + 1)*125) digitalWrite(i, HIGH);
    else digitalWrite(i, LOW);
  }
}