OBJS = lfsr.o
PROGS = lfsr_tb
SIMS = lfsr_tb.vcd
BITMAP=#lfsr.bit
UNISIM=unisim/unisim-obj93.cf
COMP=ghdl
VHDL_C=$(COMP) -i
VHDL_E=$(COMP) -m -g -Punisim --warn-unused --ieee=synopsys 
VHDL_R=$(COMP) -r
DEVEL_BASE=.
RM=rm -f
RMDIR=rm -rf

all: $(OBJS) $(PROGS) $(SIMS) $(BITMAP)

$(UNISIM) : 
	$(MAKE) -C unisim all

%.o : %.vhdl $(UNISIM)
	$(VHDL_C) $< 

%_tb : %_tb.vhdl %.o
	$(VHDL_C) $<
	$(VHDL_E) $@

%_tb.vcd : %_tb %.o
	$(VHDL_R) $< --vcd=$@

# Make instructions creating a bitmap from xilinx synthesis tools
# adapted from http://www.excamera.com/sphinx/fpga-makefile.html
project=lfsr
top_module=lfsr
vendor=xilinx
family=spartan3s
part=xc3s200a-4ft256
files=lfsr.vhdl
include $(DEVEL_BASE)/xilinx.mk

# Install the bitmap on the armadeus, by loading into the FPGA
include $(DEVEL_BASE)/install.mk
install : install_bitmap

clean :
	# Clean GHDL products
	$(RM) *.o *.cf $(PROGS) *.vcd
	# Clean Xilinx UNISIM stuff
	$(MAKE) -C unisim clean
