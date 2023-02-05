#ifndef __ThingSpeakTUBAF_H__
#define __ThingspeakTUBAF_H__

#include "AZ3166WiFi.h"
#include "http_client.h"
#include <string.h>
#include <math.h>


static bool hasWifi = false;
const char SSL_CA_PEM[] = "";


void InitWiFi()
{
  if (WiFi.begin() == WL_CONNECTED)
  {
    IPAddress ip = WiFi.localIP();
    Serial.println("Wi-Fi available");
    Serial.print("IP-Adress: ");
    Serial.println(ip.get_address());
    hasWifi = true;
  }
  else
  {
    Serial.println("No Wi-Fi");
  }
}

void updateThingSpeak(
  char ApiKey[],
  float dataForUpload[],
  int n_dataForUpload
){
  char thingSpeakUpdate[500] = "http://api.thingspeak.com/update?api_key=";
  strcat(thingSpeakUpdate, ApiKey);
  for(int i = 1; i <= n_dataForUpload; i++)
  {
    char charI[15];
    char charData[20];
    sprintf(charI, "%d", i);
    sprintf(charData, "%f", dataForUpload[i-1]);
    strcat(thingSpeakUpdate, "&field");
    strcat(thingSpeakUpdate, charI);
    strcat(thingSpeakUpdate, "=");
    strcat(thingSpeakUpdate, charData);
  }

  HTTPClient *httpClient = new HTTPClient(SSL_CA_PEM, HTTP_GET, thingSpeakUpdate);
  const Http_Response* result = httpClient->send();

  if (result == NULL)
  {
      Serial.println("Failed");
      Serial.print("Error Code: ");
      Serial.println(httpClient->get_error());
  }
  else
  {
      Serial.print("Successfully uploaded entry ");
      Serial.println(result->body);
  }
  delete httpClient;
}

#endif