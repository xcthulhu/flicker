library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library unisim;
use unisim.Vcomponents.all;

entity LFSR is
  port (
    clk  : in  std_logic;
    pout : out std_logic
    );
end;

architecture RTL of LFSR is
  signal x : std_logic := '0';
begin
  IO_L24N_3 : OBUF
    port map (I => x,
              O => pout);

  emit : process(clk)
    variable i : integer := 0;
  begin
    if rising_edge(clk) then
      if (i >= 100000000) then
        i := 0;
        x <= not x;
      end if;
    end if;
  end process;
end;
