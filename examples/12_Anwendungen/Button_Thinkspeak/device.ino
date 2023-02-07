#include "customHeaders\ThingSpeakTUBAF.h"

#define BUTTON_A_IS_PRESSED ((GPIOA->IDR & GPIO_PIN_4) == 0)
#define BUTTON_B_IS_PRESSED ((GPIOA->IDR & GPIO_PIN_10) == 0)

char apiKey[] = "XXXXXXXXXXXXXXXX";
float score_button_a = 0;
float score_button_b = 0;
unsigned long previousMillis = 0;
const long interval = 5000;

void setup() {
  InitWiFi();
  Screen.init();
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    float dataForUpload[] = {score_button_a, score_button_b};
    int n_dataForUpload = sizeof(dataForUpload)/sizeof(dataForUpload[0]);
    if(hasWifi)
    {
      updateThingSpeak(apiKey, dataForUpload, n_dataForUpload);
    }
  }

  if (BUTTON_A_IS_PRESSED){
    score_button_a++;
    delay(200);
  }
  if (BUTTON_B_IS_PRESSED){
    score_button_b++;
    delay(200);
  }
  char buff1[16];
  sprintf(buff1, "A:%s\r\n", f2s(score_button_a, 1));
  char buff2[16];
  sprintf(buff2, "B:%s\r\n", f2s(score_button_b, 1));
  Screen.print(1, buff1);
  Screen.print(2, buff2);
}