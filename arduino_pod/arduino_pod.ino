#include <Wire.h>
#include <CRC.h> // https://github.com/RobTillaart/CRC

#define ADDR_SELECT A0
#define I2C_ADDR 8
#define LED_ONBOARD 13

class input_t
{
public:
  input_t() {
    init();
  }
  input_t(int p, uint32_t d = 50) {
    init();
    pin = p;
    debounce_time = d;
    pinMode(pin, INPUT_PULLUP);
  }
  int get_state() { return state; }
  int read();
private:
  void init() {
    last_val_time = millis();
    pin = -1;
    state = last_val = 0;
  }
  
  int pin, last_val, state;
  uint32_t debounce_time, last_val_time;
};

struct cmd_t {
  uint32_t ts;
  uint16_t type;
  uint16_t len;
  // char *data;

  cmd_t() {
    type = len = 0;
    //data = NULL;
  }
};

enum state_t {
  STATE_INIT,
  STATE_RUNNING
};

char rec_buf[128];  
int blink_delay = 500;

input_t inputs[5];

#define num_sens() sizeof(inputs)/sizeof(inputs[0])

void led_setup();
void led_loop(int i, int val);
void led_delay();

void setup() {
  delay(1000); // power-up safety delay (used in some of the fastled example code)
  led_setup();

  pinMode(ADDR_SELECT, INPUT_PULLUP);
  
  if(digitalRead(ADDR_SELECT)) {
      Wire.begin(I2C_ADDR);
  } else {
      Wire.begin(I2C_ADDR + 1);
      blink_delay = 250;
  }

  for(int i=0; i<num_sens(); i++)
    inputs[i] = input_t(i+2);

  Wire.onReceive(on_receive);
  Wire.onRequest(on_request);
  Serial.begin(9600);
}

void loop() {
  // Read and debounce
  for(int i=0; i<num_sens(); i++) {
    inputs[i].read();
    led_loop(i, inputs[i].get_state());
  }

  led_delay();
  blink();
}

void blink() {
  static int last = 0;
  static bool state = false;
  
  int now = millis();
  
  if(now - last > blink_delay) {
    state = !state;
    last = now;
    digitalWrite(LED_ONBOARD, state);
  }
}

void on_receive(int num) {
  while (0 < Wire.available()) {
    char c = Wire.read();
    Serial.print(c);
  }
  Serial.println();
}

void send_init() {
  cmd_t c;
  c.ts = millis();
  c.type = 0;
  c.len = 5;

  Wire.write((char*)&c, sizeof(c));
  Wire.write((char*)"hello", c.len);
}

void send_state() {
  static int vals[num_sens()];
  static uint8_t buf[20];

  memset(buf, 0, sizeof(buf));
  
  cmd_t c;
  c.ts = millis();
  c.type = 1;
  c.len = sizeof(vals);

  memcpy(buf, &c, sizeof(c));
  int boff = sizeof(c);
  
  for(int i=0; i<num_sens(); i++) {
    *(int*)&buf[boff] = inputs[i].get_state();
    boff += sizeof(int);
  }

  uint16_t cs = crc16(buf, sizeof(buf)-2);
  *(uint16_t*)&buf[boff] = cs;

  Wire.write(buf, sizeof(buf));
}

void on_request() {
  static state_t state = STATE_INIT;

  if(state == STATE_INIT) {
    send_init();
    state = STATE_RUNNING;
    Serial.println("Initialized...");
    return;
  }

  send_state();
}

int input_t::read()
{
  if(pin < 0) // Not initialized
    return 0;
    
  int val = digitalRead(pin);
  int now = millis();

  val = !val;
  
  if(last_val != val) {
    last_val_time = now;
  }

  if(now - last_val_time > debounce_time) {
    state = val;
  }

  last_val = val;
  return state;
}
