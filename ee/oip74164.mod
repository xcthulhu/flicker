*******************************
* Begin .SUBCKT model         *
* spice-sdb ver 4.28.2007     *
*******************************
.SUBCKT oip74164 12 11 3 4 5 6 17 15 13 7 8 9 10 18 
*==============  Begin SPICE netlist of main design ============
C1 17 18 1fF  
XNCP 16 iCP INV1P
XCP 15 16 INV1P
XMR 14 1 INV1P
XNMR 13 14 INV1P
XDS 12 11 2 ANDP
X7 iCP 9 10 unconnected_pin-8 1 DFFP
X6 iCP 8 9 unconnected_pin-7 1 DFFP
X5 iCP 7 8 unconnected_pin-6 1 DFFP
X4 iCP 6 7 unconnected_pin-5 1 DFFP
X3 iCP 5 6 unconnected_pin-4 1 DFFP
X2 iCP 4 5 unconnected_pin-3 1 DFFP
X1 iCP 3 4 unconnected_pin-2 1 DFFP
X0 iCP 2 3 unconnected_pin-1 1 DFFP
.ends oip74164
*******************************
