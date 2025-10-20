// Einbinden der Bibliothek für den Sensor
#include <Arduino_APDS9960.h>

// Konfiguration (wird einmalig durchlaufen)
void setup() {
  // Sensor initialisieren
  APDS.begin();
  // LED aktivieren
  pinMode(LED_BUILTIN, OUTPUT); 
}

// Endlosschleife
void loop() {
  // Liegt eine Geste vor?
  if (APDS.gestureAvailable()) {
    // Einlesen der Geste
    int gesture = APDS.readGesture();
    // Haben wir es mit einem Links-Wish zu tuen?
    if (gesture == GESTURE_LEFT)
    {
        // Wenn ja dann Leuchte einmalig für 1s
        digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);
        digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
