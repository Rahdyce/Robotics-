#include <Wire.h>
#include "Adafruit_TCS34725.h"
float CSthreshhold = 105;
int LED_millis;
bool LED_state;
int IRLeft = 0;
int IRRight = 0;
Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);
int CS = 0;

int time1, time2 , dt;

void setup() {
  // put your setup code here, to run once:
  
  pinMode(15, INPUT);
  pinMode(14, INPUT);
  pinMode(0, OUTPUT_4MA);
  pinMode(LED_BUILTIN, OUTPUT);
  
  Wire.setSDA(20);
  Wire.setSCL(21);
  LED_millis = millis();
  Wire.begin();
  Serial.begin(57600);
  Serial.setTimeout(1);
  tcs.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  //tcs.getRGB(&red, &green, &blue);
  
  //Serial.print(red); Serial.print("\t"); Serial.print(green); Serial.print("\t"); Serial.print(blue); Serial.print("\n"); 
  /*
  time1 = millis();
  uint16_t r, g, b, c;

  tcs.getRawData(&r, &g, &b, &c);

  Serial.print("G: "); Serial.print(g, DEC); Serial.println(" ");
  
  time2 = millis();
  dt = time2 - time1;
  Serial.println(String(dt));
  */
  mediumPoll();
  Serial.println(CS);
}

void update_button() {
  if(millis() - LED_millis > 333) {
    LED_state = !LED_state;
    digitalWrite(LED_BUILTIN, LED_state);
  }
}

void mediumPoll(){
  float r, g, b;
  tcs.getRGB(&r, &g, &b);
  Serial.print(g); Serial.print("\t");
  if(g > CSthreshhold){
    CS = 1;
  }
  //Serial.print("G: "); Serial.print(g, DEC); Serial.println(" ");
}

void softPoll(int L, int R){
  IRLeft = digitalRead(L);
  IRRight = digitalRead(R);
}