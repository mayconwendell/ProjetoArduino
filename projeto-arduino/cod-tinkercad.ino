#include <Servo.h>

Servo myservo; 

void setup(){
  myservo.attach(9);
  Serial.begin(9600);
}
void loop() {
  int LDR = analogRead(A0);
  Serial.println(LDR);

  if (LDR > 300)
    myservo.write(180);
  else 
    myservo.write(0);
    
  delay(200);
}

