const int trigPin = 6;
const int echoPin = 7;

long int start = 0;
float distance = 15;
float oldDistance = 0;
int valid = 50;

float calcDist(long duration, float temp){
  float us_speed = (331.3 + (0.606 * temp)) / 1000 / 1000 * 100;
  return us_speed*duration / 2;
}

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

  distance = calcDist(micros()-start, 25);
  if ((oldDistance - distance) < 10) valid = 50;
  else valid = 0;
  
  oldDistance = distance;
  char buffer[30];
  sprintf(buffer, "distance:%d, valid:%d", int(distance), valid);
  Serial.println(buffer);

  delay(50);
}
