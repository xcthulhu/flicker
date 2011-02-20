library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.numeric_std.all;

library unisim;
use unisim.Vcomponents.all;

entity lfsr is
  port (clk  : in  std_logic;
        pout : out std_logic);
end lfsr;

architecture RTL of lfsr is
  signal x : std_logic;
begin
  IO_L24N_3 : OBUF
    port map (I => x,
              O => pout);
  
  compteur : process(clk)
      constant max_count : natural := 48000000;
      variable count : natural range 0 to max_count;
  begin
    if rising_edge(clk) then
      if count < max_count/2 then
        x  <= '1';
        count := count + 1;
      elsif count < max_count then
        x  <= '0';
        count := count + 1;
      else
        x  <= '1';
        count := 0;
      end if;
    end if;
  end process compteur;
end RTL;
