/*
 * Code to record / write sensor readings to an external SD
 * Microcontroller: Arduino Nano 33 BLE
 * 
 * Version 1.0.1
 * 
 * Created: Jan 2021 for Team 301
 */




/*------Declare Libraries-----*/
#include <Arduino_LSM9DS1.h> //For Arduino sensors
#include <SPI.h>             //For SD card
#include <SD.h>              //


/*-----Declare Variables-----*/
const int myoPin = ; // Input pin of the Myoware Sensor
float ax, ay, az;           // x, y, z readings of the accelerometer
float gx, gy, gz;           // x, y, z readings of the gyrometer
int myoVal = 0;             // Value read by myoware
int delay_Time = 1000;      // Delay time between readings



/*-----Setup the microcontroller-----*/
void setup() {
  Serial.begin(9600);
  while (!Serial) {
    //Wait for serial port to connect. Needed for native USB port only
    Serial.println("Initialization Started");
  }
  //Accelerometer / Gyrometer vibe check
        Serial.print("Initializing Accel + Gyro... ");
          if (!IMU.begin()) {
            Serial.println("IMU Failed!");
            while (1);
            }
        Serial.println(" Done!"); 
  //SD Schenanigans
        Serial.print("Initializing SD card... ");
          if (!SD.begin(4)) {
            Serial.println("SD Failed!");
            while (1);
          }
        Serial.println(" Done!"); 

  //Some jargon
        Serial.print("Accelerometer sample rate = ");
        Serial.print(IMU.accelerationSampleRate());
        Serial.println("Hz");
        Serial.print("Gyroscope sample rate = ");
        Serial.print(IMU.gyroscopeSampleRate());
        Serial.println(" Hz");
}



/*-----Start doing the do-----*/
void loop() {
  //Obtain sensor readings
    if (IMU.accelerationAvailable()) {
        IMU.readAcceleration(ax,ay, az);}
    if (IMU.gyroscopeAvailable()) {
        IMU.readGyroscope(gx, gy, gz);}
    myoVal = analogRead(myoPin);

  //Convert all readings into a string
    //CSV form is strings seperated by commas
    dataString = String(sensorReading1) + "," + String(sensorReading2) + "," + String(sensorReading3); 

  //Write readings to SD - Note: Only one file can be opened at a time
    saveData();
  //Perform readings every t seconds   
    delay(delay_Time);
}

/*-----Additional Functions-----*/
//Save data as csv file
void saveData(){
    if(SD.exists("data.csv")){                          // Check SD card is still there
        sensorData = SD.open("data.csv", FILE_WRITE);   // Open 'data.csv' file for writing
        if (sensorData){
            sensorData.println(dataString);             // Write sensor data on new line
            sensorData.close();                         // Close the file
        }}
    else{
        Serial.println("Error writing to file !");} // If SD fails
}


/*
  //Read from SD
        myFile = SD.open("test.txt");
          if (myFile) {
            Serial.println("test.txt:");
            // read from the file until there's nothing else in it:
            while (myFile.available()) {
              Serial.write(myFile.read());
            }
            // close the file:
              myFile.close();} 
          else {
            // if the file didn't open, print an error:
            Serial.println("error opening test.txt");}
*/
/*
int degreesX = 0;           // Vertical (up/down) tilt of the hand   
int degreesY = 0;           // Horizontal (left/right) tilt of the hand  
int degreesZ = 0;           // Roll of the hand
  //Calibrate x, y, z readings into degrees
  if (x > 0.1) {                        //Tilted up
    x = 100 * x;
    degreesX = map(x, 0, 97, 0, 90);}
  if (x < -0.1) {                       //Tilted down
    x = 100 * x;
    degreesX = map(x, 0, -100, 0, 90);}
  if (y > 0.1) {                        //Tilted left
    y = 100 * y;
    degreesY = map(y, 0, 97, 0, 90);}
  if (y < -0.1) {                       //Tilted right
    y = 100 * y;
    degreesY = map(y, 0, -100, 0, 90);}
  if (z > 0.1) {                        //Rolled left
    z = 100 * z;
    degreesZ = map(z, 0, 97, 0, 90);}
  if (z < -0.1) {                       //Rolled right
    z = 100 * z;
    degreesZ = map(z, 0, -100, 0, 90);
*/
}
