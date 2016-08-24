#define NUM_KNOBS 5
#define NUM_SENSORS 8

int knob[NUM_KNOBS];
int prevValue[NUM_KNOBS];
int thres = 1;

int pin[NUM_SENSORS];
int prev[NUM_SENSORS];

int pin_offset = 2;
int val = 0;



// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  for (int i = 0; i < NUM_KNOBS; i++) {
    prevValue[i] = 0;
  }
  knob[0] = A0;
  knob[1] = A1;
  knob[2] = A2;
  knob[3] = A3;
  knob[4] = A4;
  knob[5] = A5;

  for (int i = 0; i < NUM_SENSORS; i++) {
    pin[i] = i + pin_offset;
    pinMode(pin[i], INPUT);
    prev[i] = 0;
  }


}


// the loop routine runs over and over again forever:
void loop() {
  
  // Read Knobs
  
  for (int i = 0; i < NUM_KNOBS; i++) {
    // read the input on analog pin 0:
    int sensorValue = analogRead(knob[i]);
    int outVal = map(sensorValue, 0, 1023, 0, 127);

    // print out the value you read:
    if (outVal - prevValue[i] > thres ||  prevValue[i] - outVal > thres) {
      Serial.print(char(i));
      Serial.println(char(outVal));
      prevValue[i] = outVal;
    }
  }

  //Read Maraccas
  for (int i = 0; i < NUM_SENSORS; i++) {
    val = digitalRead(pin[i]);
    if (val != prev[i]) {
      Serial.print(char(i + 40));
      Serial.println(char(val));
      prev[i] = val;
    }
  }

    delay(1);        // delay in between reads for stability
}
