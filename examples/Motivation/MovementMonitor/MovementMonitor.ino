#include "Sensor.h"
#include "RGB_LED.h"

RGB_LED rgbLed;
DevI2C *i2c;
LSM6DSLSensor *sensor;
int xAxesData[3];
int prev_pos;

void setup() {
    Serial.begin(9600);//Baudrate
    i2c = new DevI2C(D14,D15);
    sensor = new LSM6DSLSensor(*i2c,D4,D5);
    sensor -> init(NULL);
    sensor -> enableAccelerator();
}

void loop() {
    sensor ->getXAxes(xAxesData);
    Serial.printf("%d %d %d\n",xAxesData[0],xAxesData[1],xAxesData[2]);
    if (xAxesData[2]<1000){
      rgbLed.setColor(255,0,0);
    }else{
      rgbLed.turnOff();
    }
    delay(50);
}
