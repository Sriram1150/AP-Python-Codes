def change(s):
    r_no = s.count('R')
    g_no = s.count('G')
    for i in s:
        if i != 'G' and i != 'R':
            raise ValueError("Only upper case R and G are excepted")
    if g_no > r_no:
        return r_no
    else:
        return g_no

print(change('R'))
print(change('RGRGR'))
print(change('GRG'))
