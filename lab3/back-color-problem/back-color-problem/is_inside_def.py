def is_inside(l_p, l_o_r):
    isinside = False
    if l_o_r[0] <= l_p[0] <= l_o_r[0]+l_o_r[2]  and l_o_r[1] <= l_p[1] <= l_o_r[1] + l_o_r[3]:
        isinside = True
    return isinside
