#include <SoftwareSerial.h>
#define rxPin 2
#define txPin 3

SoftwareSerial srl(rxPin,txPin);

void setup() {
  Serial.begin(57600);
  srl.begin(57600);
  Serial.setTimeout(1);
  srl.setTimeout(1);
}

void loop() {
  if(Serial.available() > 0){
    srl.write(Serial.read());
  }
  if(srl.available() > 0) {
    Serial.write(srl.read());
  }

}
