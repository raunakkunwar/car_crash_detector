
#include <Wire.h>
#include "MMA7660.h"
MMA7660 accelemeter;







void setup()
{
  accelemeter.init();  
  Serial.begin(9600);
}
void loop()
{
  // Initalizing the axis for the accelerometer.
  int8_t x;
  int8_t y;
  int8_t z;
  float ax,ay,az;
  accelemeter.getXYZ(&x,&y,&z);
  
  
  accelemeter.getAcceleration(&ax,&ay,&az);
  
  

  if(ax <-1.2)
  {
    Serial.println("crashisapproved");
  
  }else
  {
    Serial.println("Fine");
  }
  
  delay(50);
}
