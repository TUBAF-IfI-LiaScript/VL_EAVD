volatile int counter = 0;
volatile bool newstate = false;

void count(){
  counter++;
  newstate = true; 
}

void setup() {
  Serial.begin(9600);
  attachInterrupt(USER_BUTTON_B, count, FALLING);
}

void loop() {
  if (newstate){
    char buffer[30];
    sprintf(buffer, "Der Button wurde %3d mal gedrückt", counter);
    Serial.println(buffer);
    newstate = false;
  }
  delay(10);
}
