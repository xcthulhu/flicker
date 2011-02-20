library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.numeric_std.all;

--  A testbench has no ports.
entity lfsr_tb is end;

architecture behav of lfsr_tb is
  component lfsr is
    port (Clk  : in  std_logic;
          pout : out std_logic
          );
  end component;
  --  Specifies which entity is bound with the component.
  for dut     : lfsr use entity work.lfsr;
  signal CLK  : std_logic;
  signal pout : std_logic;
begin
  --  Component instantiation.
  dut : lfsr
    port map (CLK  => CLK,
              pout => pout) ;
  process
    -- These control the looping we will do
    constant the_end : integer := 10000;
    variable count   : integer;
  begin
    CLK <= '1';
    for count in 0 to the_end loop
      wait for 15 ns;
      CLK <= not CLK;
    end loop;
    wait;
  end process;
end;
