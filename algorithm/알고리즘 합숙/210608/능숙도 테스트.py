# chr, ord사용하면 편함 !
string = input()
alpha_cnt = {}
for alpha in string:
    alpha_cnt[alpha] = 0
print(alpha_cnt)
for alpha in string:
    alpha_cnt[alpha] += 1
for a in alpha_cnt.items():
    pass
