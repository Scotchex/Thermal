#include <Arduino.h>
char userinput;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  while(Serial.available() > 0){
    userinput = Serial.read();

      if (userinput == '1'){
        digitalWrite(13, HIGH);
      }
      else {
        digitalWrite(13, LOW);
      }
  }

}