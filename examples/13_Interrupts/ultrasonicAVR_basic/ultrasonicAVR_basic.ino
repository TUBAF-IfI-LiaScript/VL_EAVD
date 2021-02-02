const int trigPin = 6;
const int echoPin = 7;

long int start = 0;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  //Lösung aus der Literatur für den Arduino UNO, MEGA usw
  //duration = pulseIn(echoPin, HIGH);
  //Serial.println(duration);

  while(digitalRead(echoPin) == LOW);
  start = micros();
  while(digitalRead(echoPin) == HIGH);

  Serial.println(micros()-start);

  delay(50);
}
