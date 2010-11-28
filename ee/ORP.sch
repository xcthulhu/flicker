v 20091004 2
C 40000 40000 0 0 0 title-B.sym
C 48400 46500 1 0 1 spice-subcircuit-IO-1.sym
{
T 47500 46900 5 10 0 1 0 6 1
device=spice-IO
T 47550 46750 5 10 1 1 0 6 1
refdes=P1
}
C 48400 46100 1 0 1 spice-subcircuit-IO-1.sym
{
T 47500 46500 5 10 0 1 0 6 1
device=spice-IO
T 47550 46350 5 10 1 1 0 6 1
refdes=P2
}
C 50400 46300 1 0 0 spice-subcircuit-IO-1.sym
{
T 51300 46700 5 10 0 1 0 0 1
device=spice-IO
T 51250 46550 5 10 1 1 0 0 1
refdes=P3
}
C 44100 48100 1 0 0 spice-subcircuit-LL-1.sym
{
T 44200 48400 5 10 0 1 0 0 1
device=spice-subcircuit-LL
T 44200 48500 5 10 1 1 0 0 1
refdes=A1
T 44200 48200 5 10 1 1 0 0 1
model-name=ORP
}
T 50100 40800 9 10 1 0 0 0 2
SPICE subcircuit for digital OR
(in 6 CMOS transistors)
T 50100 40400 9 10 1 0 0 0 1
ORP.sch
T 50400 40100 9 10 1 0 0 0 1
1
T 52100 40100 9 10 1 0 0 0 1
1
T 54100 40100 9 10 1 0 0 0 1
Matthew P. Wampler-Doty
C 48100 46300 1 0 0 NORP-1.sym
{
T 48600 47000 5 10 1 1 0 0 1
refdes=X1
T 49200 47700 5 10 0 1 0 0 1
device=NORP
T 49200 47500 5 10 0 0 0 0 1
model-name=NORP
T 49200 47900 5 10 0 0 0 0 1
symversion=1.0
T 50200 47300 5 10 0 0 0 0 1
footprint=none
}
C 49500 46300 1 0 0 INV1P-1.sym
{
T 49900 46900 5 10 1 1 0 0 1
refdes=X2
T 50300 48000 5 10 0 1 0 0 1
device=INV1P
T 50300 47800 5 10 0 0 0 0 1
model-name=INV1P
T 50300 47000 5 10 0 0 0 0 1
symversion=1.0
T 50300 46300 5 10 0 0 0 0 1
footprint=none
}
C 41400 49000 1 0 0 ORP-1.sym
{
T 42100 49900 5 10 0 0 0 0 1
device=ORP
T 42100 51300 5 10 0 0 0 0 1
model-name=ORP
T 41400 49000 5 10 0 0 0 0 1
graphical=1
}
