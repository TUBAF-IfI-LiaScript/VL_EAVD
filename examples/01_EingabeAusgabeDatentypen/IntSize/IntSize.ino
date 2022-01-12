void setup() {
  Serial.begin(9600);//Baudrate
  int x;
  Serial.println("---------------");
  Serial.print("int x umfasst ");
  Serial.print((unsigned int)sizeof x);
  Serial.print(" Byte.");
}

void loop() {
}
