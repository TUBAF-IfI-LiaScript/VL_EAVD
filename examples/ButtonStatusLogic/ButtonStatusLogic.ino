int buttonAState;
int buttonBState;
 
void setup(){
  pinMode(USER_BUTTON_A, INPUT);
  pinMode(USER_BUTTON_B, INPUT);
  pinMode(RGB_R, OUTPUT);
 } 
  
void loop() {
  buttonAState = digitalRead(USER_BUTTON_A);
  buttonBState = digitalRead(USER_BUTTON_B);
  if ( !buttonAState && !buttonBState){
    digitalWrite(RGB_R, HIGH);
    delay(3000); 
  }
  else
  {
    digitalWrite(RGB_R, LOW); 
  }
}
  
