
int pin_led = 7;

void setup() {
  Serial.begin(9600);
  pinMode(pin_led, OUTPUT);
  digitalWrite(pin_led,LOW);
}

void loop() {

  String command = Serial.readString();

  if(command == "accendi"){
    // accendo il led
    digitalWrite(pin_led,HIGH);
  } else if(command == "spegni") {
    // spengo il led
    digitalWrite(pin_led,LOW);
  } else {
     Serial.println("Comando non riconosciuto");
  }
  
}
