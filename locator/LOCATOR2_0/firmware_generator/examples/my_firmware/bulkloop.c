

#include <stdio.h>

#include <fx2regs.h>
#include <fx2macros.h>
#include <serial.h>
#include <delay.h>
#include <autovector.h>
#include <lights.h>
#include <setupdat.h>
#include <eputils.h>


#define SYNCDELAY SYNCDELAY4
#define REARMVAL 0x80
#define REARM() EP2BCL=REARMVAL



volatile WORD bytes;
volatile __bit gotbuf;
volatile BYTE icount;
volatile __bit got_sud;
DWORD lcount;
__bit on;



//https://www.triplespark.net/elec/periph/USB-FX2/software/io_examples.html
static void Initialize(void)
{
    CPUCS = 0x12;  // 48MHz, output to CLKOUT signal enabled.

    // Internally clocked (48MHz) sync slave fifo mode.
    // Output to IFCLK not enabled (set bit5 to enable).
    IFCONFIG = 0xE3;  SYNCDELAY;  //11100011
    REVCTL = 0x03;    SYNCDELAY;  // See TRM...

    // Configure EP6 (IN) for bulk input, quad-buffered (4*512 bytes).
    EP6CFG = 0xE0;  SYNCDELAY; //11100000
    // Configure EP2 (OUT) for bulk output, double-buffered (2*512 bytes).
    EP2CFG = 0xA2; SYNCDELAY; //10100010

    EP4CFG = 0x00;
    SYNCDELAY;
    EP8CFG = 0x00;
    SYNCDELAY;

    FIFORESET = 0x80;  SYNCDELAY;  // NAK all requests from host.
    FIFORESET = 0x02;  SYNCDELAY;  // Reset individual EP (2,4,6,8)
    FIFORESET = 0x06;  SYNCDELAY;
    FIFORESET = 0x00;  SYNCDELAY;  // Resume normal operation.



    // Configure EP6 for AUTOIN, 8bit wide bus, EP2 for AUTOOUT 8 bit wide.
    EP6FIFOCFG = 0xC;  SYNCDELAY; //00001100  00001100
    EP2FIFOCFG = 0x14; SYNCDELAY; //00010100


    // PORTACFG: FLAGD SLCS(*) 0 0 0 0 INT1 INT0
    PORTACFG = 0x00;  SYNCDELAY; // (delay maybe not needed)

    // All default polarities: SLWR active low,...
    FIFOPINPOLAR=0x00;  SYNCDELAY;

    // This determines how much data is accumulated in the FIFOs before a
    // USB packet is committed. Use 512 bytes to be sure.
    EP6AUTOINLENH = 0x02; SYNCDELAY;  // MSB
    EP6AUTOINLENL = 0x00; SYNCDELAY;  // LSB



}

void main()
{
    USBCS |= 0x08;
    Initialize();
    EA = 1;       // Enable All Interrupts (Глобальное разрешение прерываний 8051)
    USBIE = 1;    // Enable USB Interrupts

    // 4. Подключаемся обратно к USB с НОВЫМИ дескрипторами (Инициируем ReNumeration)
    USBCS &= ~0x08;

    for(;;) {
    if ( got_sud )
        {
            handle_setupdata(); // Отвечаем хосту, отдаем PID 1004 из dscr.a51
            got_sud = FALSE;    // Сбрасываем флаг для следующего запроса
        }

    }
}







// copied routines from setupdat.h

BOOL handle_get_descriptor(void) {
  return FALSE;
}

// value (low byte) = ep
#define VC_EPSTAT 0xB1

BOOL handle_vendorcommand(BYTE cmd) {

 switch ( cmd ) {

     case VC_EPSTAT:
        {
         __xdata BYTE* pep= ep_addr(SETUPDAT[2]);
         printf ( "ep %02x\n" , *pep );
         if (pep) {
          EP0BUF[0] = *pep;
          EP0BCH=0;
          EP0BCL=1;
          return TRUE;
         }
        }
     default:
          printf ( "Need to implement vendor command: %02x\n", cmd );
 }
 return FALSE;
}

// this firmware only supports 0,0
BOOL handle_get_interface(BYTE ifc, BYTE* alt_ifc) {
 printf ( "Get Interface\n" );
 if (ifc==0) {*alt_ifc=0; return TRUE;} else { return FALSE;}
}
BOOL handle_set_interface(BYTE ifc, BYTE alt_ifc) {
 printf ( "Set interface %d to alt: %d\n" , ifc, alt_ifc );

 if (ifc==0&&alt_ifc==0) {
    // SEE TRM 2.3.7
    // reset toggles
    RESETTOGGLE(0x02);
    RESETTOGGLE(0x86);
    // restore endpoints to default condition
    RESETFIFO(0x02);
    EP2BCL=0x80;
    SYNCDELAY;
    EP2BCL=0X80;
    SYNCDELAY;
    RESETFIFO(0x06);
    SYNCDELAY;

    return TRUE;
 } else
    return FALSE;
}

// get/set configuration
BYTE handle_get_configuration(void) {
 return 1;
 }
BOOL handle_set_configuration(BYTE cfg) {
 return cfg==1 ? TRUE : FALSE; // we only handle cfg 1
}


// copied usb jt routines from usbjt.h
void sudav_isr(void) __interrupt (SUDAV_ISR) {

  got_sud=TRUE;
  CLEAR_SUDAV();
}

__bit on5;
__xdata WORD sofct=0;
void sof_isr (void) __interrupt (SOF_ISR) __using (1) {
    ++sofct;
    if(sofct==8000) { // about 8000 sof interrupts per second at high speed
        on5=!on5;
        if (on5) {d5on();} else {d5off();}
        sofct=0;
    }
    CLEAR_SOF();
}

void usbreset_isr(void) __interrupt (USBRESET_ISR) {
    handle_hispeed(FALSE);
    CLEAR_USBRESET();
}
void hispeed_isr(void) __interrupt (HISPEED_ISR) {
    handle_hispeed(TRUE);
    CLEAR_HISPEED();
}

