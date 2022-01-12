#include <OledDisplay.h>
volatile long int startTime = 0;
volatile long int endTime = 0;
volatile bool result = false;

void start(){
  startTime = millis();
  Screen.clean();
}

void finished(){
  endTime = millis();
  result = true;
}

void setup() {
  Serial.begin(9600);
  Screen.init();
  attachInterrupt(USER_BUTTON_A, start, RISING);
  attachInterrupt(USER_BUTTON_B, finished, RISING);
  Serial.println("Das Spiel beginnt");
}

void loop() {
  if (result){
    char buffer[30];
    sprintf(buffer, "Delay %d [ms]", endTime-startTime);
    Serial.println(buffer);
    result = false;
    Screen.print(buffer);
  }
  
  // Hier passiert irgendwas 
  
  delay(10);
}
