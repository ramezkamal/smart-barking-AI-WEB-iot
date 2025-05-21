const int irSensor1 = 2;
const int irSensor2 = 3;
const int irSensor3 = 4;
const int irSensor4 = 5;
const int buzzer = 8;

void setup() {
    pinMode(irSensor1, INPUT);
    pinMode(irSensor2, INPUT);
    pinMode(irSensor3, INPUT);
    pinMode(irSensor4, INPUT);
    pinMode(buzzer, OUTPUT);
}

void loop() {
    // قراءة القيم من المستشعرات
    int sensor1 = digitalRead(irSensor1);
    int sensor2 = digitalRead(irSensor2);
    int sensor3 = digitalRead(irSensor3);
    int sensor4 = digitalRead(irSensor4);
    
    // إذا اكتشف أي مستشعر شيئًا أمامه، يعمل البازر
    if (sensor1 == LOW || sensor2 == LOW || sensor3 == LOW || sensor4 == LOW) {
        digitalWrite(buzzer, HIGH);
    } else {
        digitalWrite(buzzer, LOW);
    }
}
