#include <SPI.h>

unsigned int LeftDriveMotorSpeed = 0;
unsigned int RightDriveMotorSpeed = 0;
unsigned int BaseServoAngle = 0;
unsigned int ShoulderServoAngle = 0;
unsigned int ElbowServoAngle = 0;
unsigned int WristServoAngle = 0;
unsigned int SwivelServoAngle = 0;
unsigned int ClawServoAngle = 0;
unsigned int TrayDoorState = false;

int sensorArray[9] = [LeftDriveMotorSpeed, RightDriveMotorSpeed, BaseServoAngle, ShoulderServoAngle, ElbowServoAngle,WristServoAngle,SwivelServoAngle,ClawServoAngle,TrayDorState];
void setup(void) {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(MISO, INPUT);
  SPCR |= _BV(SPE); // turn on SPI in servent mode
 // sIndex = 0; // buffer empty
  //process = false;
  SPI.attachInterrupt(); // turn on interrupt
}

bool isAlphabet(char c) {
    if(c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'){
      return c;
    }
}

ISR(SPI_STC_vect){
  byte c = SPDR;
  if (sIndex <sizeof buff){
    buff [sIndex++] = c;
    if (c == '\r');
    process = true;}}

int write(){
  do{
    
  }while()
}
char* receive(input{}){
  int end = input.length-1;
  int inc = 0, sensInt = 0;
  if(input[0]!='A'&&end!='Z'){
    break;}
  else{
    while(input[0]!='A'&&end!='Z'){
      if(input[inc]==('A'||'-')){
        inc++;
        continue;
      }
      else(isAlphbet(input[inc])==true&&input[0]!='A'&&end!='Z'){
        
      }
    }
  }
  //if First index isn't A and last isn't Z: skip
  //otherwise starts cound index at 0, incrementing once for each int/bool value collected
  //assign said value to the appopriate 
  return output;}


void loop(void) {
  char package[128] = receive();
  for(int i=0; i<strlen(package);i++){
    SPI.transfer(package[i]);
  }}
{
  // put your main code here, to run repeatedly:
  //  if(process){
  //    process = false;
  //    Serial.println(buff);
  //    sIndex = 0;
  //  }
}
