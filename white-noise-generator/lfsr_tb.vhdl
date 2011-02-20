library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.numeric_std.all;

--  A testbench has no ports.
entity lfsr_tb is end;

architecture behav of lfsr_tb is
  component lfsr is
    port (clk  : in  std_logic;
          pout : out std_logic
          );
  end component;
  --  Specifies which entity is bound with the component.
  for dut     : lfsr use entity work.lfsr;
  signal clk  : std_logic;
  signal pout : std_logic;
begin
  --  Component instantiation.
  dut : lfsr
    port map (clk  => clk,
              pout => pout) ;
  process
    -- These control the looping we will do
    constant the_end : integer := 10000;
    variable count   : integer;
  begin
    clk <= '1';
    for count in 0 to the_end loop
      wait for 15 ns;
      clk <= not clk;
    end loop;
    wait;
  end process;
end;
