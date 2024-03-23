#include <CommandFactory.h>
#include <MotorFactory.h>

#define basePin 0
#define shoulderPin 1
#define elbowPin 2
#define wristPin 3
#define swivelPin 4
#define clawPin 5
#define trayPin 26
#define vp1 27
#define vp2 28

#define leftmotp 7
#define leftmotn 6
#define rightmotp 8
#define rightmotn 9
#define leftmots 10
#define rightmots 11

#define relayp 22

CommandFactory Command;
MotorFactory Motor;

bool runstop = true;
String received = "hi";
String ALLSTOP = "A-L=127-R=127-B=26-S=84-E=0-R=144-W=82-C=60-TD=90-X=0-Z";

int LEDTime, oldLEDTime;
int LEDTiming = 333;
bool LEDState = true;

Servo vanity1;
Servo vanity2;

void setup() {
  Command.interpret(ALLSTOP);
  state();
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(relayp, OUTPUT_12MA);
  digitalWrite(relayp, HIGH);
  Serial1.setTX(16);
  Serial1.setRX(17);
  Serial1.begin(57600);
  Serial1.setTimeout(2);
  Motor.setServoPins(basePin, shoulderPin, elbowPin, wristPin, swivelPin, clawPin, trayPin, relayp);
  Motor.setMotorPins(leftmotp, rightmotp, leftmotn, rightmotn, leftmots, rightmots);
  Motor.setDrive(3, 127);
  oldLEDTime = millis();
  //testDrive();
  vanity1.attach(vp1, 500,2500);
  vanity2.attach(vp2, 500,2500);
  vanity1.write(90);
  vanity2.write(90);
}

void loop() {
  board_led();
  test2();
  state();
}

void test2() {
  while(runstop) {
    board_led();
    if(Serial1.available() > 0) {
    received = Serial1.readStringUntil('\n');
    Command.interpret(received);
    runstop = false;
    }
  }
  runstop = true;
  Serial1.println("ECHO: "  + Command.command());
}

void state() {
  for(int i = 0; i < 10; i++) {
    Motor.set(i, Command.reader(i));
  }
}

void board_led() {
  LEDTime = millis();
  if((LEDTime - oldLEDTime) > LEDTiming) {
    oldLEDTime = millis();
    LEDState = !LEDState;
  }
  digitalWrite(LED_BUILTIN, LEDState);
}

void testDrive() {
  digitalWrite(leftmotp, HIGH);
  digitalWrite(leftmotn, LOW);
  digitalWrite(rightmotp, HIGH);
  digitalWrite(rightmotn, LOW);
  analogWrite(rightmots, 255);
  analogWrite(leftmots, 255);
}
