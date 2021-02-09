const int trigPin = 16;
const int echoPin = 5;

long int start = 0;
float distance = 15;
float oldDistance = 0;
int valid = 50;

float calcDist(long duration, float temp){
  float us_speed = (331.3 + (0.606 * temp)) / 1000 / 1000 * 100;
  return us_speed * duration / 2;
}

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  while(digitalRead(echoPin) == LOW);
  start = micros();
  while(digitalRead(echoPin) == HIGH);

  distance = calcDist(micros()-start, 25);
  
  oldDistance = distance;
  Serial.print("distance:");
  Serial.println(distance,2);
  delay(50);
}
