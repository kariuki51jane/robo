const int analogIn0 = A0;
const int analogIn1 = A1;

int mVperAmp = 185; // use 100 for 20A Module and 66 for 30A Module
double RawValue= 0;
double RawValue2= 0;
float ACSoffset = 2500; 
double Voltage = 0;
double Voltage2 = 0;
double Amps = 0;
int count=0;

double BatteryVoltage=0;
double Energy=2000;


void setup(){ 
 Serial.begin(9600);
}

void loop(){
 RawValue=0;
 RawValue2=0;

 for (int i=0;i<1000;i++){
  RawValue +=analogRead(analogIn1);
  RawValue2 +=analogRead(analogIn0);
  
  delay(1);
 }
 
 RawValue/=1000;
 RawValue2/=1000;  

 Voltage = (RawValue / 1024.0) * 5000; 
 Voltage2 = (RawValue / 1024.0) * 5000*4;


 Amps = ((Voltage - ACSoffset) / mVperAmp);

 if(count==2){
  ACSoffset=Voltage;
 }
 
 if(count>2 && -0.05<Amps && Amps<0.05){
    ACSoffset=Voltage;
 }
 

 Serial.print("Amps = "); // shows the voltage measured 
 Serial.print(Amps,3); // the '3' after voltage allows you to display 3 digits after decimal point
 Serial.print("\t Voltage = "); // shows the voltage measured 
 Serial.println(Voltage2,3); // the '3' after voltage allows you to display 3 digits after decimal point

 count++;

}

