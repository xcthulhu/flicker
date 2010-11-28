* gnetlist -g spice-sdb -o flicker.mod lfsr.sch rc-ladder.sch
*********************************************************
* Spice file generated by gnetlist                      *
* spice-sdb version 4.28.2007 by SDB --                 *
* provides advanced spice netlisting capability.        *
* Documentation at http://www.brorson.com/gEDA/SPICE/   *
*********************************************************
*==============  Begin SPICE netlist of main design ============
C10 0 22 47nF  
R10 21 22 1k  
C9 0 21 47nF  
R9 20 21 1k  
C8 0 20 47nF  
R8 19 20 1k  
C7 0 19 47nF  
R7 18 19 1k  
C6 0 18 47nF  
R6 17 18 1k  
C5 0 17 47nF  
R5 16 17 1k  
C4 0 16 47nF  
R4 15 16 1k  
C3 0 15 47nF  
R3 14 15 1k  
C2 0 14 47nF  
R2 13 14 1k  
C1 0 13 47nF  
R1 lfsr_out 13 1k  
X8 11 12 2 ORP
RA 0 12 100  
CA Vcc 12 1uF  
X7 10 3 11 XORP
X6 9 4 10 XORP
X5 lfsr_out 7 9 XORP
X4 8 8 unconnected_pin-19 unconnected_pin-20 unconnected_pin-21 unconnected_pin-22 0 1 Vcc unconnected_pin-23 unconnected_pin-24 unconnected_pin-25 lfsr_out Vcc oip74164
X3 6 6 unconnected_pin-13 unconnected_pin-14 unconnected_pin-15 unconnected_pin-16 0 1 Vcc unconnected_pin-17 unconnected_pin-18 7 8 Vcc oip74164
X2 5 5 unconnected_pin-6 unconnected_pin-7 unconnected_pin-8 unconnected_pin-9 0 1 Vcc unconnected_pin-10 unconnected_pin-11 unconnected_pin-12 6 Vcc oip74164
X1 2 2 3 4 unconnected_pin-1 unconnected_pin-2 0 1 Vcc unconnected_pin-3 unconnected_pin-4 unconnected_pin-5 5 Vcc oip74164
Vclk 1 0 pulse 0 3.3V 10n 10n 10n 5u 12.5u
.end
