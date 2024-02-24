#include "sensorFactory.h"
const int LEFT_IR_PIN = 3;  // Pin connected to the left IR sensor
const int RIGHT_IR_PIN = 2; // Pin connected to the right IR sensor

void setup() {
  Serial.begin(9600);
  pinMode(LEFT_IR_PIN, INPUT);
  pinMode(RIGHT_IR_PIN, INPUT);
}

void loop() {
  int leftIrValue = digitalRead(LEFT_IR_PIN);
  int rightIrValue = digitalRead(RIGHT_IR_PIN);
  
  // Check if both sensors detect the line
  if (leftIrValue == LOW && rightIrValue == LOW) {
    Serial.println("On track");
  } 
  // Check if the left sensor detects the line
  else if (leftIrValue == LOW && rightIrValue == HIGH) {
    Serial.println("Turn right");
  } 
  // Check if the right sensor detects the line
  else if (leftIrValue == HIGH && rightIrValue == LOW) {
    Serial.println("Turn left");
  } 
  // If both sensors do not detect the line
  else {
    Serial.println("Lost track");
  }
  
  delay(2000); // Adjust delay as needed
}
