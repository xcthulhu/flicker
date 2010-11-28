models = oip74164.mod XORP.mod XOR.mod ORP.mod OR.mod flicker.mod
all: $(models)

flicker.mod : lfsr.sch rc-ladder.sch
	gnetlist -g spice-sdb lfsr.sch rc-ladder.sch -o $@

%.mod : %.sch
	gnetlist -g spice-sdb $< -o $@

clean :
	rm *.mod *.sch~
