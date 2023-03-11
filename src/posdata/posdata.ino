#include <Wire.h>
#include <LSM6.h>
#include <LPS.h>
LSM6 imu;
LPS ps;

char report[80];

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  
  if (!imu.init())
  {
    Serial.println("Failed to detect and initialize IMU!");
    while (1);
  }
  imu.enableDefault();

    if (!ps.init())
  {
    Serial.println("Failed to autodetect pressure sensor!");
    while (1);
  }

  ps.enableDefault();
}

void loop() {
  // put your main code here, to run repeatedly:
  float pressure = ps.readPressureMillibars();
  float altitude = ps.pressureToAltitudeMeters(pressure);
  float temperature = ps.readTemperatureC();
  
  imu.read();

  snprintf(report, sizeof(report), "A: %6d %6d %6d    G: %6d %6d %6d",
    imu.a.x, imu.a.y, imu.a.z,
    imu.g.x, imu.g.y, imu.g.z);
  Serial.println(report);

  
  Serial.print("p: ");
  Serial.print(pressure);
  Serial.print(" mbar\ta: ");
  Serial.print(altitude);
  Serial.print(" m\tt: ");
  Serial.print(temperature);
  Serial.println(" deg C");

  delay(100);
}
