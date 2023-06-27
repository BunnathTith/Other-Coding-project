#include <Servo.h>
Servo ServoX, ServoY;
int X=A0;
int Y=A2;
void setup() {
  // put your setup code here, to run once:
  ServoX.attach(2, 500, 2450);
  ServoY.attach(7, 450, 2830);
  pinMode(X, INPUT);
  pinMode(Y, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int aX=analogRead(X);
  int aY=analogRead(Y);
  ServoX.writeMicroseconds(map(aX, 0, 1023, 500, 2450));
  ServoY.writeMicroseconds(map(aY, 0, 1023, 450, 2830));
    
}
