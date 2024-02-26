#include <CommandFactory.h>

CommandFactory cmd;

char vals[9] = {'L','R','B','S','E','R','W','C','T'};
int eater[9];
bool runstop = true;
const int numIndexes = 9;
String argnames[numIndexes] = {"LMSpeed","RMSpeed","baseAngle","shoulderAngle","elbowAngle","wristAngle","swivelAngle","clawAngle","trayDoor"};
String received = "hi";

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
}

void loop() {
  test2();
}

void test2() {
  Serial.println("ENTER FULL COMMAND STRING");
  while(runstop) {
    if(Serial.available() > 0) {
    received = Serial.readString();
    runstop = false;
    }
  }
  runstop = true;
  Serial.println("ECHO: " + received);
  cmd.interpret(received);
  received = cmd.command();
  Serial.println("CMD: " + received);
}

void eat(int arr[])
{
  int numIndexes = 9;
  String argnames[9] = {"LMSpeed","RMSpeed","baseAngle","shoulderAngle","elbowAngle","wristAngle","swivelAngle","clawAngle","trayDoor"};
  for(int i = 0; i < numIndexes; i++) {
    cmd.writer(i, arr[i]);
  }
}

void test1() {
  Serial.println(cmd.command());
  for(int i = 0; i < 9; i++) {
    Serial.println(argnames[i]);
    runstop = true;
    while(runstop) {
      if(Serial.available() > 0) {
        eater[i] = Serial.readString().toInt();
        Serial.println("RECEIVED: " + String(eater[i]));
        cmd.writer(i, eater[i]);
        Serial.println("CMD: " + cmd.reader(i));
        runstop = false;
      }
    }
  } 
}
