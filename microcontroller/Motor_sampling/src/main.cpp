#include <Arduino.h>
#include <Wire.h>
#include "AS5600.h"

AS5600 as5600;

// Define the analog input pin
const int analogPin = A0; // Change this to the pin you're using

void setup() {
 Serial.begin(115200); // Start serial communication at 115200 baud
 Wire.begin(); // Initialize I2C communication

 if (!as5600.begin()) { // Check if the sensor is successfully initialized
    Serial.println("Failed to connect to AS5600 sensor."); // Print error message if connection fails
 } else {
    Serial.println("Connected to AS5600 sensor."); // Print success message if connection is successful
 }
}

void loop() {
 uint16_t rawAngle = as5600.readAngle(); // Read the raw angle
 float angleDegrees = rawAngle * AS5600_RAW_TO_DEGREES; // Convert to degrees
 Serial.print("Angle: ");
 Serial.print(angleDegrees);
 Serial.println("°"); // Send the angle over serial

 int analogValue = analogRead(analogPin); // Read the analog input
 //Serial.print("Analog Value: ");
 //Serial.println(analogValue); // Print the analog value

 delay(1000); // Wait for 1 second
}
