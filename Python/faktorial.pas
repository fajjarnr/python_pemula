program Faktorial;
uses crt;
var
i, angka, f : interger;
begin
clrscr;
write ('Masukan sebuah angka <1-7>='); readln(angka);
f:=1;
for i := angka downto 1 do
f:=f*i;
writeln(angka,'!=',f);
readln;
end