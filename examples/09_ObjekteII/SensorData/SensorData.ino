#include "OledDisplay.h"
#include "Sensor.h"

// Peripherals 
static DevI2C *ext_i2c;
static LSM6DSLSensor *accelgyroSensor;
static RGB_LED rgbLed;

// Accelerometer, pedometer variables
static int xAxesData[3];
static int gAxesData[3];

void setup()
{
  Screen.init();
  Screen.print(0, "Initializing...");
  Screen.print(1, " > Serial interface");
  Serial.begin(115200);
   
  // Initialize the motion sensor
  Screen.print(2, " > Motion sensor     ");
  ext_i2c = new DevI2C(D14, D15);
  accelgyroSensor = new LSM6DSLSensor(*ext_i2c, D4, D5);
  accelgyroSensor->init(NULL); 
  accelgyroSensor->enableAccelerator();
}

void loop()
{
  accelgyroSensor->getXAxes(xAxesData);
  //Serial.printf("Accelerometer X Axes: x=%d, y=%d, z=%d\n", xAxesData[0], xAxesData[1], xAxesData[2]);
  Serial.printf("%d %d %d\n", xAxesData[0], xAxesData[1], xAxesData[2]);
  delay(50);
}
