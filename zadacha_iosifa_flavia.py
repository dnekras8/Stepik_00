def mas_killing(mass, step, pos):
    new_mass = mass[:]
    new_pos = pos
    temp_step = (step - 1)
    while new_pos + temp_step < len(new_mass):
        if len(new_mass) == 1: #one must stay alive
            break
        new_pos += temp_step
        new_mass.pop(new_pos )
    new_pos = new_pos - len(new_mass)
    if len(new_mass) == 1:
        return new_mass
    else:
        return mas_killing(new_mass, step, new_pos)

#print(*[i for i in range(16)])
nm = 5
st = 2
m = [i+1 for i in range(nm)]
print(m)
print(mas_killing(m,st,0)[0])