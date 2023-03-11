#include <Servo.h> 

Servo plunger_motor;

int servoPin = 3; 

int plunger_pos



void setup() {
  plunger_motor.attach(servoPin);
}

void intake(){
  plunger_motor.write(180);
  sleep(1000);
  plunger_motor.write(90);
}

void expell(){
  plunger_motor.write(0);
  sleep(1000);
  plunger_motor.write(90);
}
