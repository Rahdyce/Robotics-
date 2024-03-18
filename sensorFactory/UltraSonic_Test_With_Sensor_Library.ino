#include <sensorFactory.h>

sensorFactory ultra0;
sensorFactory ultra1;
sensorFactory ultra2;
sensorFactory ultra3;

void setup() {
  // put your setup code here, to run once:
  ultra0.setUltraPin(1,0,0);
  ultra1.setUltraPin(3,2,1);
  ultra2.setUltraPin(4,5,2);
  ultra3.setUltraPin(15,14,3);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    Serial.println(ultra0.sonicDistanceSensor(0,1));
    Serial.println(ultra1.sonicDistanceSensor(2,3));
    Serial.println(ultra2.sonicDistanceSensor(5,4));
    Serial.println(ultra3.sonicDistanceSensor(14,15));
}
