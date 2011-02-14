library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity LFSR is
  port (
    clk  : in  std_logic;
    nout : out std_logic;
    pout : out std_logic
    );
end;

architecture RTL of LFSR is
  signal hist : std_logic_vector(55 downto 0) := (others => '1');
begin
  nout <= '0';
  emit : process(clk)
  begin
    if rising_edge(clk) then
      hist <= hist(hist'high-1 downto 0) & (hist(24) xor hist(55));
    end if;
  end process;
  pout <= hist(hist'high);
end;
