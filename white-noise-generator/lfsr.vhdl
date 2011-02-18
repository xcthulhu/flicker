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
  signal hist : std_logic_vector(55 downto 0) := (others => '1');
begin  
  IO_L24N_3 : OBUF
    port map (I => hist(hist'high),
              O => pout);

  emit : process(clk)
  begin
    if rising_edge(clk) then
      -- See Knuth's "Art of Computer Programming: Volume 2", pg. 27
      hist <= hist(hist'high-1 downto 0) & (hist(24) xor hist(55));
    end if;
  end process;
end;
