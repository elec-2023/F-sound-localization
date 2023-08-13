#include <Arduino.h>

int led =25;
int cnt=600;
int arr1[600];
int arr2[600];
int arr3[600];
int pointer=0;
UART pc1(4, 5, NC, NC);   
UART &pc = pc1;

int adcs[] = {26, 27, 28};
void digitalToggle(int pin)
{
 digitalWrite(pin, !digitalRead(pin));
}
void setup()
{
  // put your setup code here, to run once:
 pc.begin(115200);
}

void loop()
{

 for(int i = 0; i < 100000; i++){
 arr1[pointer] = analogRead(27);
 arr2[pointer] = analogRead(26);
 arr3[pointer]= analogRead(28);
 pointer++;
 if (pointer==600){
  pointer=0;
 }
 if(arr1[pointer-1]>250||arr2[pointer-1]>250||arr3[pointer-1]>250)
 {
  if (pointer==600){
  pointer=0;
 }
 for(int i = 1; i < 300; i++)
 {
 arr1[pointer] = analogRead(27);
 arr2[pointer] = analogRead(26);
 arr3[pointer] = analogRead(28);
 pointer++;
 if (pointer==600){
  pointer=0;
 }
 }
 pc.println("a1:");
 for(int i = 0; i < 600; i++){
 pc.print(arr1[pointer]);
 pc.print(",");
 pointer++;
 if (pointer==600){
  pointer=0;
 }
 }
 pc.println(".");
 pc.println("a2:");
 for(int i = 0; i < 600; i++){
 pc.print(arr2[pointer]);
 pc.print(",");
  pointer++;
 if (pointer==600){
  pointer=0;
 }
 }
 pc.println(".");
 pc.println("a3:");
 for(int i = 0; i < 600; i++){
 pc.print(arr3[pointer]);
 pc.print(",");
  pointer++;
 if (pointer==600){
  pointer=0;
 }
 }
 pc.println(".");
 }
 if (pointer==600){
  pointer=0;
 }
 }
}