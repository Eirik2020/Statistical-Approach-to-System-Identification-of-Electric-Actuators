// PlatformIO project setup for Arduino Mega
// Ensure your platformio.ini is set up correctly for Arduino Mega

#include <Arduino.h>

// Define analog pin
const int analogPin = A15;

void setup() {
 // Initialize serial communication at 9600 baud
 Serial.begin(9600);
}

void loop() {
 // Read the analog value
 int sensorValue = analogRead(analogPin);

 // Print the value to the serial port
 Serial.println(sensorValue);

 // Wait for a bit before taking the next reading
 delay(100);
}
