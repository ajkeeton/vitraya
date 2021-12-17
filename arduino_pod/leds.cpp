#include <FastLED.h>

#define LED_PIN     10
#define NUM_LEDS    12
#define MIN_BRIGHT  3
#define MAX_BRIGHT  255
#define LED_TYPE    WS2811
#define COLOR_ORDER RGB
CRGB leds[NUM_LEDS];

#define LED_UPDATES_PER_SECOND 100

CRGBPalette16 currentPalette;
TBlendType    currentBlending;

extern CRGBPalette16 myRedWhiteBluePalette;
extern const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM;
void SetupTotallyRandomPalette();
void FillLEDsFromPaletteColors(uint8_t, uint8_t);
void new_palette();

void led_setup() {
  
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip);
  FastLED.setBrightness(MAX_BRIGHT);
  
  //currentPalette = RainbowColors_p;
  //currentPalette = CloudColors_p;
  currentPalette = PartyColors_p;
  currentBlending = LINEARBLEND;
}

void led_loop(int idx, int val) {
  // if(idx != 0) return;
  
  static int startIndex = 0;
  static uint8_t brightness = MIN_BRIGHT;
  static bool triggered = false;

  if(!val) {
    if(brightness > MIN_BRIGHT)
      brightness -= 3;
    triggered = false;
  }
  else {
    if(brightness >= MAX_BRIGHT) {
       if(triggered) {
        //new_palette();
        // XXX Do something interesting ... flash?
        triggered = false;
       }
    }
    else {
      brightness++;
      triggered = true;
    }
  }

  if(brightness < MIN_BRIGHT)
    brightness = MIN_BRIGHT;
    
  startIndex++;

  FillLEDsFromPaletteColors(startIndex, brightness);
}

void led_delay() {
  FastLED.show();
  FastLED.delay(1000 / LED_UPDATES_PER_SECOND);
}

void FillLEDsFromPaletteColors(uint8_t colorIndex, uint8_t brightness)
{
    for( int i = 0; i < NUM_LEDS; i++) {
        leds[i] = ColorFromPalette( currentPalette, colorIndex, brightness, currentBlending);
        colorIndex += 3;
    }
}

// This function fills the palette with totally random colors.
void SetupTotallyRandomPalette()
{
    for( int i = 0; i < 16; i++) {
        currentPalette[i] = CHSV( random8(), 255, random8());
    }
}

// This function sets up a palette of black and white stripes,
// using code.  Since the palette is effectively an array of
// sixteen CRGB colors, the various fill_* functions can be used
// to set them up.
void SetupBlackAndWhiteStripedPalette()
{
    // 'black out' all 16 palette entries...
    fill_solid( currentPalette, 16, CRGB::Black);
    // and set every fourth one to white.
    currentPalette[0] = CRGB::White;
    currentPalette[4] = CRGB::White;
    currentPalette[8] = CRGB::White;
    currentPalette[12] = CRGB::White;
    
}

// This function sets up a palette of purple and green stripes.
void SetupPurpleAndGreenPalette()
{
    CRGB purple = CHSV( HUE_PURPLE, 255, 255);
    CRGB green  = CHSV( HUE_GREEN, 255, 255);
    CRGB black  = CRGB::Black;
    
    currentPalette = CRGBPalette16(
                                   green,  green,  black,  black,
                                   purple, purple, black,  black,
                                   green,  green,  black,  black,
                                   purple, purple, black,  black );
}


// This example shows how to set up a static color palette
// which is stored in PROGMEM (flash), which is almost always more
// plentiful than RAM.  A static PROGMEM palette like this
// takes up 64 bytes of flash.
const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM =
{
    CRGB::Red,
    CRGB::Gray, // 'white' is too bright compared to red and blue
    CRGB::Blue,
    CRGB::Black,
    
    CRGB::Red,
    CRGB::Gray,
    CRGB::Blue,
    CRGB::Black,
    
    CRGB::Red,
    CRGB::Red,
    CRGB::Gray,
    CRGB::Gray,
    CRGB::Blue,
    CRGB::Blue,
    CRGB::Black,
    CRGB::Black
};

// There are several different palettes of colors demonstrated here.
//
// FastLED provides several 'preset' palettes: RainbowColors_p, RainbowStripeColors_p,
// OceanColors_p, CloudColors_p, LavaColors_p, ForestColors_p, and PartyColors_p.
//
// Additionally, you can manually define your own color palettes, or you can write
// code that creates color palettes on the fly.  All are shown here.

void new_palette()
{
  static int8_t idx = -1;
  idx++;
  switch(idx) {
    case 0:
      currentPalette = RainbowColors_p;
      currentBlending = LINEARBLEND;
      break;

    case 1:
    //  SetupPurpleAndGreenPalette();
    //  currentBlending = LINEARBLEND;
    //  break;
      idx++;
    case 2:
      currentPalette = RainbowColors_p;
      currentBlending = LINEARBLEND; 
      break;

    case 3:
      currentPalette = RainbowStripeColors_p;   
      currentBlending = NOBLEND;
      break;

    case 4:
      currentPalette = RainbowStripeColors_p;
      currentBlending = LINEARBLEND;
      break;

    case 5:
      SetupBlackAndWhiteStripedPalette();       
      currentBlending = NOBLEND;
      break;

    case 6:
      SetupBlackAndWhiteStripedPalette();
      currentBlending = LINEARBLEND;
      break;

    case 7:
      currentPalette = CloudColors_p;
      currentBlending = LINEARBLEND;
      break;

    case 8:
      currentPalette = PartyColors_p;
      currentBlending = LINEARBLEND;
      break;
      
    default:
      idx = -1;
  }
 
  /*
    uint8_t secondHand = (millis() / 1000) % 60;
    static uint8_t lastSecond = 99;
    
    if( lastSecond != secondHand) {
        lastSecond = secondHand;
        if( secondHand ==  0)  { currentPalette = RainbowColors_p;         currentBlending = LINEARBLEND; }
        if( secondHand == 10)  { currentPalette = RainbowStripeColors_p;   currentBlending = NOBLEND;  }
        if( secondHand == 15)  { currentPalette = RainbowStripeColors_p;   currentBlending = LINEARBLEND; }
        if( secondHand == 20)  { SetupPurpleAndGreenPalette();             currentBlending = LINEARBLEND; }
        if( secondHand == 25)  { SetupTotallyRandomPalette();              currentBlending = LINEARBLEND; }
        if( secondHand == 30)  { SetupBlackAndWhiteStripedPalette();       currentBlending = NOBLEND; }
        if( secondHand == 35)  { SetupBlackAndWhiteStripedPalette();       currentBlending = LINEARBLEND; }
        if( secondHand == 40)  { currentPalette = CloudColors_p;           currentBlending = LINEARBLEND; }
        if( secondHand == 45)  { currentPalette = PartyColors_p;           currentBlending = LINEARBLEND; }
        if( secondHand == 50)  { currentPalette = myRedWhiteBluePalette_p; currentBlending = NOBLEND;  }
        if( secondHand == 55)  { currentPalette = myRedWhiteBluePalette_p; currentBlending = LINEARBLEND; }
    }
    */
}
