#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into digital pin 2 on the Arduino
#define ONE_WIRE_BUS 2

// Setup a oneWire instance to communicate with any OneWire device
OneWire oneWire(ONE_WIRE_BUS);  

// Pass oneWire reference to DallasTemperature library
DallasTemperature sensors(&oneWire);

int deviceCount = 0;
float tempC;

void setup(void)
{
  sensors.begin();  // Start up the library
  Serial.begin(9600);
  sensors.setResolution(12);
  // locate devices on the bus
  deviceCount = sensors.getDeviceCount();
}

void loop(void)
{ 
  // Send command to all the sensors for temperature conversion
  sensors.requestTemperatures(); 
  
  // Display temperature from each sensor
  for (int i = 0;  i < deviceCount;  i++)
  {
    Serial.print("Sensor");
    Serial.print(i+1);
    Serial.print(",");
    tempC = sensors.getTempCByIndex(i);
    Serial.print(tempC);
    Serial.print("C,");    
  }
  Serial.println("");
}
