*******************************
* Begin .SUBCKT model         *
* spice-sdb ver 4.28.2007     *
*******************************
.SUBCKT XORP 2 3 4 
*==============  Begin SPICE netlist of main design ============
M6 4 3 1 Vss pch  l=0.4u w=1.2u
M5 4 3 2 Vdd1 nch  l=0.4u w=1.2u
M3 4 1 3 Vss nch  l=0.4u w=1.2u
M4 4 2 3 Vdd1 pch  l=1u w=10u
M2 1 2 Vss1 Vss pch  l=0.4u w=1.2u
M1 1 2 Vdd1 Vdd1 nch  l=0.4u w=1.2u
.ends XORP
*******************************
