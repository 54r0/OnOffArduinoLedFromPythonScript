
int pin_led = 7;
int pin_button = 8;
int lettura = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pin_led, OUTPUT);
  digitalWrite(pin_led,LOW);
}

void loop() {

  

  Serial.println("ciao");
  

  // accendo il led

}
