#include <OledDisplay.h>
#include <Sensor.h>

// Peripherals
DevI2C ext_i2c(D14,D15);
LSM6DSLSensor accelgyroSensor(ext_i2c,D4,D5);
RGB_LED rgbLed;

// Accelerometer, pedometer variables
int xAxesData[3];
int gAxesData[3];

void setup()
{
Screen.init();
  Screen.print(0, "Initializing ...");
  Screen.print(1, " > Serial interface");
  Serial.begin(115200);
  
  // Initialize the motion sensor
  Screen.print(2, " > Motion sensor ");
  accelgyroSensor.init(NULL);
  accelgyroSensor.enableAccelerator();
}

void loop()
{
  accelgyroSensor.getXAxes(xAxesData);
  Serial.printf("X_Axes:%d, Y_Axes:%d, Z_Axes:%d\n", xAxesData[0], xAxesData[1], xAxesData[2]);
  //Serial.printf("%d %d %d\n", xAxesData[0], xAxesData[1], xAxesData[2]);
  delay(50);
}
