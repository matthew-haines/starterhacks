#define trig 10
#define echo 8

long duration;
int distance;

void setup() {
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

void loop() {
  digitalWrite(trig, LOW); //reset for better error
  delayMicroseconds(5);
  
  digitalWrite(trig, HIGH); //send out a pulse for 10 milliseconds
  delayMicroseconds(10);
  digitalWrite(trig, LOW); //end pulse

  duration = pulseIn(echo, HIGH); //wait and read pulse back from from ultrasonic, calculate time taked to receive pulse
  
  distance= duration*0.034/2; //distance based on speed of sound :)

  // if(distance < 400 && > 50){
    
  // }
  
  delay(1000);
}