
void setup() {
  Serial.begin(115200); 

  char buffer[60];
  char name[] = "ProzProg";
  //formatieren des Textes und ablegen in dem Array
  sprintf(buffer, "Der Zahlenwert ist %5.3f und der String %s", 5.45, name);
  Serial.println(buffer);
}

void loop() {
}
