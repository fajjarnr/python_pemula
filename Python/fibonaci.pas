program fibonaci;
begin
clrscr;
write('Masukan jumlah deret : ');readln(n);
writeln;
write('Deret fibonaci ',n,' Deret : ');
x:=1;
y:=1;
z:=1;
i:=1;
while(i<=n) do
begin
write(z,'');
i:=i+1;
z:=x+y;
x:=y;
y:=z;
end;
readln;
end.