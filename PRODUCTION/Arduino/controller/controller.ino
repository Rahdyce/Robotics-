#include <Toggle.h>
#include <CommandFactory.h>
#include <SoftwareSerial.h>

#define mini 500
#define maxi 2500
#define runpin 7
#define BOARD_LED 13
#define lbutton 9
#define rbutton 8
#define toggleswitch 10
#define trayswitch 7

#define trayhigh 138
#define traylow 20

int a, b, c, d, e, f,g,h;
double da,db,dc,dd,de,df,dg,dh;
double na,nb,nc,nd,ne,nf,ng,nh;
int accel, steer, l,r;
double acoeff, scoeff;
String printer = " ";
String A = " a: ";
String B = " b: ";
String C = " c: ";
String D = " d: ";
String E = " e: ";
String F = " f: ";
String T = " BOOL: ";
double const numc =  0.1764707;
double const numb = 0.2490234;
int const deadband = 5;
bool runState = true;
int counter, timecount1, timecount2;
int dcount = 0;
double tps = 0.0;

int LEDTime, oldLEDTime;
int LEDTiming = 333;
bool LEDState;

// example command: A-L=0-R=1-B=0-S=1-E=999-R=45-W=0-C=58-TD=0-Z

CommandFactory cmd;

char vals[9] = {'L','R','B','S','E','R','W','C','T'};
int eater[9];
bool runstop = true;
const int numIndexes = 9;
String argnames[numIndexes] = {"LMSpeed","RMSpeed","baseAngle","shoulderAngle","elbowAngle","wristAngle","swivelAngle","clawAngle","trayDoor"};
String received = "hi";
String ALLSTOP = "A-L=127-R=127-B=26-S=84-E=0-R=144-W=82-C=60-TD=90-X=0-Z";

int counter1, counter2;

const int rxPin = 2;
const int txPin = 3;
SoftwareSerial srl(rxPin,txPin);
Toggle lbut(lbutton);
Toggle rbut(rbutton);

void setup() {
  pinMode(BOARD_LED, OUTPUT);
  pinMode(lbutton, INPUT);
  pinMode(rbutton, INPUT);
  pinMode(toggleswitch, INPUT);
  pinMode(trayswitch, INPUT);
  Serial.begin(57600);
  Serial.setTimeout(1);
  srl.begin(57600);
  srl.setTimeout(1);
  da = ((double)analogRead(A0));
  db = ((double)analogRead(A1));
  dc = ((double)analogRead(A2));
  dd = ((double)analogRead(A3));
  de = ((double)analogRead(A6));
  df = ((double)analogRead(A7));
  lbut.begin(lbutton);
  rbut.begin(rbutton);
  lbut.setToggleState(0);
  rbut.setToggleState(0);
  lbut.setToggleTrigger(1);
  rbut.setToggleTrigger(1);
}

void loop() {
  timecount1 = millis();
  buttonfunc();
  runner1();
  sender();
  recievefrompico();
  board_led();
  timecount2 = millis();
  counter++;
  dcount = (timecount2 - timecount1);
  tps = 1000.0 / (double) dcount;
  Serial.println("TPS: " + String(tps) + " LN: " + String(counter) + " DC: " + dcount);
}

void recievefrompico() {
  counter1 = millis();
  while(runstop) {
    board_led();
    buttonfunc();
    counter2 = millis();
    if(counter2 - counter1 > 1000) {
      Serial.println("WAITING FOR PICO");
      break;
    }
    if(srl.available() > 0) {
      received = srl.readString();
      runstop = false;
      Serial.print(received);
    }
  }
  runstop = true;
}

void test2() {
  Serial.println("ENTER FULL COMMAND STRING");
  while(runstop) {
    board_led();
    buttonfunc();
    if(Serial.available() > 0) {
    received = Serial.readStringUntil('\n');
    runstop = false;
    }
  }
  runstop = true;
  Serial.println("ECHO: " + received);
  cmd.interpret(received);
  sender();
}

void sender() {
  if(!digitalRead(toggleswitch)) {
    received = cmd.command();
  } else {
    received = ALLSTOP;
  }
  Serial.println("CMD: " + received);
  srl.println(received);
}

void runner1() {
  na = ((double)analogRead(A4));
  nb = ((double)analogRead(A5));
  nc = ((double)analogRead(A0));
  nd = ((double)analogRead(A1));
  ne = ((double)analogRead(A2));
  nf = ((double)analogRead(A3));
  ng = ((double)analogRead(A6));
  nh = ((double)analogRead(A7));
  if(na > da + deadband || na < da - deadband) {
    da = na;
  }
  if(nb > db + deadband || nb < db - deadband) {
    db = nb;
  }
  if(nc > dc + deadband || nc < dc - deadband) {
    dc = nc;
  }
  if(nd > dd + deadband || nd < dd - deadband) {
    dd = nd;
  }
  if(ne > de + deadband || ne < de - deadband) {
    de = ne;
  }
  if(nf > df + deadband || nf < df - deadband) {
    df = nf;
  }
  if(ng > dg + deadband || ng < dg - deadband) {
    dg = ng;
  }
  if(nh > dh + deadband || nh < dh - deadband) {
    dh = nh;
  }
  a = da * numb;
  b = db * numb;
  c = dc * numc;
  d = dd * numc;
  e = de * numc;
  f = df * numc;
  g = dg * numc;
  h = dh * numc;
  carsteer();
  printer = A + a + B + b + C + c + D + d + E + e + F + f + T + runState;
  if(lbut.toggle()) {
    a = 127;
    b = 127;
  }
  cmd.writer(0,a);
  cmd.writer(1,b);
  cmd.writer(2,c);
  cmd.writer(3,d);
  cmd.writer(4,e);
  cmd.writer(5,f);
  cmd.writer(6,g);
  cmd.writer(7,h);
  if(!digitalRead(trayswitch)) {
    cmd.writer(8,traylow);
  } else {
    cmd.writer(8,trayhigh);
  }
  cmd.writer(9,rbut.toggle());
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

void board_led() {
  LEDTime = millis();
  if((LEDTime - oldLEDTime) > LEDTiming) {
    oldLEDTime = millis();
    LEDState = !LEDState;
  }
  digitalWrite(BOARD_LED, LEDState);
}

void buttonfunc() {
  lbut.poll();
  rbut.poll();
}

void carsteer() {
  accel = 127 - b;
  steer = a - 127;
  acoeff = 1.0 - ((double) abs(steer) / (double) 127);
  if(accel > 20 || accel < -20) {
    if(steer > 0 ) {
      l = accel*acoeff;
      r = accel;
    } else if(steer < 0) {
      r = accel*acoeff;
      l = accel;
    } else {
      r = accel;
      l = accel;
    }
  } else {
    if(steer < 20 ) {
      l = -127*acoeff + 127;
      r = -l;
    } else if(steer > -20) {
      r = -127*acoeff + 127;
      l = -r;
    } else {
      r = 0;
      l = 0;
    }
  }
  a = l + 127;
  b = r + 127;
}
