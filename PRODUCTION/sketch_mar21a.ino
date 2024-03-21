#include <Wire.h>
#include "Adafruit_TCS34725.h"
#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

VL53L0X_RangingMeasurementData_t measure1;
VL53L0X_RangingMeasurementData_t measure2;

int time1, time2, dt;
int LED_millis;
bool LED_state;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.setSDA(20);
  Wire.setSCL(21);
  Wire.begin();
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(0, OUTPUT_4MA);
  for(int i = 0; i < 10; i ++){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
  }
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(0, HIGH);

  digitalWrite(0, LOW);

  //Serial.print("Milk");
  /*
  if(!lox.begin(0x29)) {
    Serial.println(F("Failed to boot second VL53L0X"));
    while(1);
  }
  */
}

void update_button() {
  if(millis() - LED_millis > 333) {
    LED_state = !LED_state;
    digitalWrite(LED_BUILTIN, LED_state);
  }
  Serial.print("Milk");
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(0, HIGH);
  delay(1000);
  digitalWrite(0, LOW);
  update_button();
  Serial.print("milk: ");
  //lox.rangingTest(&measure1);
  Serial.println(measure1.RangeStatus);
}
