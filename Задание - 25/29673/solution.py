"""
Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу. Найдите все
натуральные числа, принадлежащие отрезку [123456789;223456789] и имеющие ровно три нетривиальных делителя. Для каждого
найденного числа запишите в ответе его наибольший нетривиальный делитель.
Ответы расположите в порядке возрастания.

Например, в диапазоне [5;16] ровно три различных нетривиальных делителя имеет число 16, поэтому для этого диапазона
вывод на экране должна содержать следующие значения:
16 8
"""

from math import sqrt

for i in range(123456789, 223456789 + 1):
    sqrtI = sqrt(i)
    k = 0
    if int(sqrtI) == sqrtI:
        max_k = 0
        for j in range(2, int(sqrtI) - 1):
            if i % j == 0:
                if max_k == 1:
                    max_k = i // j
                k += 2

    if k == 2:
        print(i, max_k)


"""
var
    i, del: integer;
    control: boolean;
begin
    del := 2;
    i := round(power(289123456, 0.25));
    while (power(i, 4) <= 389123456) do begin
        while (i mod del <> 0) do begin
            del := del + 1;
            if (i < 3) or (del = i) then control := True
            else control := False;
        end;
        if control then writeln(power(i, 4), ' ', power(i, 3));
        i := i + 1;
        del := 2;
        control := False;
    end;
end.
В"""





