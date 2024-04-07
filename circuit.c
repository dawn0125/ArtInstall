#include  "msp430.h"
#include  "math.h"
#define     LED1                  BIT0                         //for P1.0
#define     LED2                  BIT7                         //for P4.7
#define     BUTTON                BIT1
#define     TXD                   BIT4                      // TXD on P4.4
#define     RXD                   BIT5                      // RXD on P4.5
#define     PreAppMode            0
#define     RunningMode           1
void InitializeButton(void);
void InitializeTXD(void);
void InitializeLED(void);
void PreApplicationMode(void);
void ConfigureUART_output_only(void);
volatile unsigned int TXByte = 0;
volatile unsigned int Mode;
volatile unsigned int start = 0;
volatile unsigned int end = 0;
volatile unsigned int delta = 0;
volatile unsigned int distance = 0;
volatile unsigned short int hits = 0;


void main(void)
{
  WDTCTL = WDTPW | WDTHOLD;                 // Stop WDT

    //Initialize output to sonar Trigger
    P1DIR |= BIT2; // Output on Pin 1.2
    P1SEL |= BIT2; // Pin 1.2 selected as PWM
    TA0CTL = TASSEL_2 | MC_1 | ID_3;   // Timer A control set to SMCLK, 1MHz and count up mode MC_1
    TA0CCTL1 |= OUTMOD_7; //classic PWM
    TA0CCR0 = 0xFFFF; // Period up to 65ms (Sonar doc recommends ~60ms between trigger pulses)
    TA0CCR1 = 10; // duty cycle 10 us (Sonar doc recommends for trigger pulse)



  InitializeButton();
  InitializeLED();
  InitializeTXD();
  Mode = PreAppMode;
 __enable_interrupt();      // Enable interrupts.
  PreApplicationMode();          // Blinks LEDs, waits for button press
  ConfigureUART_output_only();

//  __bis_SR_register(GIE); // Enable global interrupts

  //P2.0 defaults to input
  P2SEL |= BIT0; // set to input timer (P2.0 has TA1.1 see schema)
  TA1CTL = TASSEL_2 | MC_2; //SMCLK 1MHZ clock, continuous mode counting
  TA1CCTL1 = CAP | CCIE | CM_3 | SCS | CCIS_0;

  /* Main Application Loop */
  while(1)
  {
    TXByte = TXByte + 1;
    while (! (UCA0IFG & UCTXIFG)); // wait for TX buffer to be ready for new data

      distance = delta / 58; //returns value in cm
//    UCA1TXBUF = distance; //Transmit TXByte;
      UCA1TXBUF = distance;

    //P1OUT ^= LED1;  // toggle the light every time we make a measurement.
    //P4OUT &= ~LED2;
    __delay_cycles(100000);
  }
}

void ConfigureUART_output_only(){
    /* Configure hardware UART */
    UCA1CTL1 = UCSWRST; //Recommended to place USCI in reset first
    P4SEL |= BIT4 + BIT5;
    UCA1CTL1 |= UCSSEL_2; // Use SMCLK
    UCA1BR0 = 109; // Set baud rate to 9600 with 1.048MHz clock (Data Sheet 36.3.13)
    UCA1BR1 = 0; // Set baud rate to 9600 with 1.048MHz clock
    UCA1MCTL = UCBRS_2; // Modulation UCBRSx = 2
    UCA1CTL1 &= ~UCSWRST; // Initialize USCI state machine
    /* if we were going to receive, we would also:
       IE2 |= UCA1RXIE; // Enable USCI_A1 RX interrupt
    */
}

void PreApplicationMode(void) {
  P1DIR |= LED1;
  P4DIR |= LED2;
  P1OUT |= LED1;                 // To enable the LED toggling effect
  P4OUT &= ~LED2;

  while (Mode == PreAppMode) {
    P1OUT ^= LED1;
    P4OUT ^= LED2;                      // toggle the two lights.
    _delay_cycles (500000);             //This function introduces 0.5 s delay
    }
}

void InitializeLED(void){
    P1DIR |= LED1;
    P4DIR |= LED2;
    P1OUT &= ~LED1;     //LEDs off
    P4OUT &= ~LED2;
}

void InitializeTXD(void){
    P4DIR |= TXD;
    P4OUT |= TXD;
}

void InitializeButton(void)  // Configure Push Button
{
  P1DIR &= ~BUTTON;
  P1OUT |= BUTTON;
  P1REN |= BUTTON;
  P1IES |= BUTTON;
  P1IFG &= ~BUTTON;
  P1IE |= BUTTON;
}

/* *************************************************************
 * Port Interrupt for Button Press
 * 1. During standby mode: to enter application mode
 *
 * *********************************************************** */

void __attribute__ ((interrupt(PORT1_VECTOR))) PORT1_ISR(void) // Port 1 interrupt service routine
 {                                                    //code of the interrupt routine goes here
    Mode = RunningMode;

    P1IE &= ~BUTTON;         // Disable port 1 interrupts
    P1IFG &= ~0b00000010;        // Clear P1.1 IFG.If you don't, it just happens again.
 }


#pragma vector=TIMER1_A1_VECTOR
__interrupt void Timer_A(void)
 {
    switch (hits){
    case 0:
        start = TA1CCR1;
        break;
    case 1:
        end = TA1CCR1;
        delta = end - start;
        hits = 0;
        break;
    }
    hits = hits + 1;
    TA1CCTL1 &= ~CCIFG;
 }
