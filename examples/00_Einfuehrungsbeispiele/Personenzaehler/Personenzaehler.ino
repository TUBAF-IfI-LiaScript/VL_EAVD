#define PIN_TRIGGER 12
#define PIN_ECHO    13

// Überwachungsbereich in cm
const int RANGE_MIN = 30;      // Untere Grenze
const int RANGE_MAX = 60;      // Obere Grenze

const unsigned long DEBOUNCE_TIME = 1000; // ms - Mindestzeit zwischen Zählungen
const int STABILIZATION_DELAY = 50;    // ms

bool personDetected = false;
unsigned int peopleCount = 0;
unsigned long lastCountTime = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_TRIGGER, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  Serial.println("Person Counter with defined range started");
}

unsigned int getDistance() {
  digitalWrite(PIN_TRIGGER, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIGGER, LOW);

  unsigned long duration = pulseIn(PIN_ECHO, HIGH, 25000); // Timeout 25ms (~4m)
  unsigned int distance = duration / 58;
  return distance;
}

void loop() {
  unsigned int distance = getDistance();
  unsigned long currentTime = millis();

  // Prüfen, ob sich etwas im Überwachungsbereich befindet
  bool inRange = (distance >= RANGE_MIN && distance <= RANGE_MAX);

  // Eintritt in den Bereich erkannt
  if (inRange && !personDetected) {
    personDetected = true;
    Serial.println("Person entered monitoring zone");
  }

  // Verlassen des Bereichs
  if (!inRange && personDetected) {
    if (currentTime - lastCountTime > DEBOUNCE_TIME) {
      peopleCount++;
      lastCountTime = currentTime;
      Serial.print("Person counted. Total = ");
      Serial.println(peopleCount);
    }
    personDetected = false;
  }

  delay(STABILIZATION_DELAY);
}
