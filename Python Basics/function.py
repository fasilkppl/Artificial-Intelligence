toms_exp = [100, 200, 300]
bobs_exp = [500, 600, 700]


def calc_total_exp(exp):
    total = 0
    for item in exp:
        total = total+item
    return total
        


toms_total = calc_total_exp(toms_exp)
bobs_total = calc_total_exp(bobs_exp)

print('toms total exp: ', toms_total)
print('bobs total exp: ', bobs_total)




