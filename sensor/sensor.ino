#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,2,3,4,5);
//https://www.facebook.com/doyouknowarduino/videos/491839614333641/
void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
}
 
void loop()
{
  int light=analogRead(0);
  lcd.clear();
  lcd.print("Light : ");
  lcd.print(light);
  Serial.println(light);
  delay(500);
}
