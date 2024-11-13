// List of Command 
/*
 * Serial Commands [command, pinouts, data, x, y, z]
 * 1 read sensor
 * 2 write actuator
 * 3 register sensor
 * 4 register actuator
 * 
*/


int pulse[2] = {2, 3};
int dir[3] = {24, 26, 28};
long currX = 0; long currY = 0; long targetX = 0; long targetY = 0;
bool dirX = true; bool dirY = true;
uint8_t rec[2];
uint8_t received = 0xFF;
uint8_t finished = 0x00;
bool isRunning = false;
long currM; long delayM = 50; long prevM = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Start");
  pinMode(pulse[0], OUTPUT);
  pinMode(pulse[1], OUTPUT);
  pinMode(dir[0], OUTPUT);
  pinMode(dir[1], OUTPUT);
  pinMode(dir[2], OUTPUT);
}

void loop() {
  if(!isRunning){
    if(Serial.available() > 0){
      Serial.readBytes(rec, 2);
      Serial.write(received);
      targetX = (rec[0]*796);
      targetY = (rec[1]*796);
      dirX = (targetX > currX) ? true : false;
      dirY = (targetY > currY) ? true : false;
      digitalWrite(dir[0], dirX);
      digitalWrite(dir[1], !dirX);
      digitalWrite(dir[2], dirY);
      isRunning = true;
    }
  } else {
    if(targetX != currX){
      runMotor(pulse[0]);
      currX = targetX;
    }
    if(targetY != currY){
      runMotor(pulse[1]);
      currY = targetY;
    }
    isRunning = (targetY == currY && targetX == currX) ? false : true;
    if(!isRunning){
      Serial.write(finished);
    }
  }
}

void runMotor(int pin, int steps, int current) {
  int target = abs(steps - current);

  for (int i = 0; i < target; i++) {
    digitalWrite(pin, HIGH);
    delayMicroseconds(400);
    digitalWrite(pin, LOW);
    delayMicroseconds(500);
  }
}
void runMotor(int pin) {
  currM = micros();
  if(prevM >= currM){
    digitalWrite(pin, HIGH);
    delayMicroseconds(400);
    digitalWrite(pin, LOW);
    prevM = currM;
  }
}