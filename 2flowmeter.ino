#define interval 5    // Measuring period
int supPin = 2;   //This is the Supply pin on the Arduino
int retPin = 3;   //Return pin
double result;    //This is the value we intend to calculate. 
volatile int supflow;   //This integer needs to be set as volatle to ensure it updates correctly during the interrupt process. 
volatile int retflow;

void setup() {
  // put your setup code here, to run once:
  pinMode(supPin, INPUT);   //Sets the Supply pin as an input
  pinMode(retPin, INPUT);   //Sets the Return pin as an input
  attachInterrupt(0, supply, RISING);   //Configures interrupt 0 (pin 2 on the Arduino Uno) to run the function "supply"  
  attachInterrupt(1, retour, RISING);   //Configures interrupt 1 (pin 3 on the Arduino Uno) to run the function "retour" 
  Serial.begin(9600);   //Start Serial
  }
void loop() { 
  supflow = 0;      // Resets pulse counters to 0
  retflow = 0;

  interrupts();   //Enables interrupts
  delay (interval * 1000);    //Wait seconds
  noInterrupts();   //Disables interrupts
   
  //Start the math
  result = (supflow-retflow) * 0.1;   //Calculates Consumption in mL over specified interval
  Serial.print("CONS,");
  Serial.print(result * 3.6 / interval);   //Calcucalates Consumption in L/Hr
  Serial.print(",");
  Serial.print(result);
  result = supflow * 0.1 * 3.6 / interval;   //Calculates Supply in L/Hr
  Serial.print(",SUP,");
  Serial.print(result);
  result = retflow * 0.1 * 3.6 / interval;   //Calculates Retour in L/Hr
  Serial.print(",RET,");
  Serial.print(result);
  Serial.print(",");
  Serial.print(interval);
  Serial.println();
}
 
void supply()
{
   supflow++;   //Every time this function is called, increment "Supply" by 1
}

void retour()
{
  retflow++;    //Every time this function is called, increment "Retour" by 1
  }
