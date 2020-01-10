#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

#define FIREBASE_HOST "coin-collector-7dd3f.firebaseio.com"
#define FIREBASE_AUTH "zKl75JtBLTnwEamC3iRWqZHfFXDHmiVkzomSYfEY"

#define WIFI_SSID "zoher"
#define WIFI_PASSWORD "ahmedzoher"

int ENA_R = 14;
int IN1_R = 12;
int IN2_R = 13;

int ENA_L = 15;
int IN1_L = 0;
int IN2_L = 2;

int middlePin = 5;
int leftPin = 16;
int rightPin = 4;

int LED = 10;

String Car1;
int counter= 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

Serial.print("Connecting");

while (WiFi.status() != WL_CONNECTED) {
Serial.print(".");
delay(500);
}

pinMode(ENA_R, OUTPUT);
pinMode(IN1_R, OUTPUT);
pinMode(IN2_R, OUTPUT);

pinMode(ENA_L, OUTPUT);
pinMode(IN1_L, OUTPUT);
pinMode(IN2_L, OUTPUT);

pinMode(middlePin, INPUT);
pinMode(rightPin, INPUT);
pinMode(leftPin, INPUT);

pinMode(LED, OUTPUT);

Serial.println();
Serial.println("Connected.");

Serial.println(WiFi.localIP());

Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

int Size1= Firebase.getInt("/rotate1size/");
for (int i = 0; i<Size1; i++) {
  String s = String("/rotate1/")+i;
  Car1= Car1 + Firebase.getString(s);
}
for (int i=0; i<Size1; i++) {
Serial.println(Car1);
}
//Car1= "RFPLLFD";
//Serial.println(Car1);
}

void Left() {
  analogWrite (ENA_R, 506);
  analogWrite (ENA_L, 506);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, HIGH);
  digitalWrite (IN1_L, HIGH);
  digitalWrite (IN2_L, LOW);
  delay(425);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(200);
}

void Right() {
  analogWrite (ENA_R, 506);
  analogWrite (ENA_L, 506);
  digitalWrite (IN1_R, HIGH);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, HIGH);
  delay(425);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(200);
}

void Move_Forward() {
  analogWrite (ENA_R, 506);
  analogWrite (ENA_L, 506);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, HIGH);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, HIGH);
  delay(50);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(100);
}

void Rotate(){
  analogWrite (ENA_R, 506);
  analogWrite (ENA_L, 506);
  digitalWrite (IN1_R, HIGH);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, HIGH);
  delay(750);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(200);
}

void Up(){
  analogWrite (ENA_R, 506);
  analogWrite (ENA_L, 506);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, HIGH);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, HIGH);
  delay(150);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(200);
}

void Stop() {
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(1500);
}

void Center() {

  if(!(digitalRead(leftPin)) && !(digitalRead(rightPin)))     // Move Forward
  {
  analogWrite (ENA_R, 506);
  analogWrite (ENA_L, 506);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, HIGH);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, HIGH);
  delay(50);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);








  digitalWrite (IN2_L, LOW);
  delay(100);
  }
  
  if(!(digitalRead(leftPin)) && (digitalRead(rightPin)))     // Turn right
  {
  analogWrite (ENA_R, 0);
  analogWrite (ENA_L, 506);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, HIGH);
  delay(50);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(100);
    
  }
  
  if((digitalRead(leftPin)) && !(digitalRead(rightPin)))     // Turn left
  {
  analogWrite (ENA_R, 506);
  analogWrite (ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, HIGH);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(50);
  analogWrite(ENA_R, 0);
  analogWrite(ENA_L, 0);
  digitalWrite (IN1_R, LOW);
  digitalWrite (IN2_R, LOW);
  digitalWrite (IN1_L, LOW);
  digitalWrite (IN2_L, LOW);
  delay(100);
  
  }
  
}



void loop() {
  // put your main code here, to run repeatedly:

if(digitalRead(rightPin) && digitalRead(leftPin)){
  if(Car1.charAt(counter)=='F'){
//    Firebase.setString("Message","FORWARD");
    Move_Forward();
    Up();
  }
  else if(Car1.charAt(counter)=='R'){
//    Firebase.setString("Message","RIGHT");
    Stop();
    Right();
    Up();
    counter= counter+1;
  }
  else if(Car1.charAt(counter)=='L'){
//    Firebase.setString("Message","LEFT");
    Stop();
    
      if (Car1.charAt(counter+1)!='L'){
      Left();
      Up();
      counter= counter+1;
    }else {
      Rotate();
      Up();
      counter= counter+1;
    }
    

    
  }
  else if(Car1.charAt(counter)=='P'){
//    Firebase.setString("Message","PICK UP");
    digitalWrite(LED,HIGH);
//    Stop();
//    Left();
//    Stop();
//    Left();
//    Stop();

    Stop();
    Rotate();
    Up();
    counter= counter+3;
  }
  else if(Car1.charAt(counter)=='D'){
//    Firebase.setString("Message","DROP");
    digitalWrite(LED,LOW);
    Stop();
  }
  counter= counter+1;


}

else if (!(digitalRead(middlePin))){
//  Firebase.setString("Message","CENTER");
  Center();
}

else {
//  Firebase.setString("Message","MOVE");
  Move_Forward();

}
}
