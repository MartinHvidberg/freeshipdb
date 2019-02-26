

with open(r"../data/numbers711.csv", "r") as fili:
    lst_hit = fili.readlines()

print("Found: {} nunmbers".format(len(lst_hit)))

cnt_good = 0
for imo in lst_hit:
    # Check IMO check-digit nnnnnnP
    str_imo = str(imo).strip()  # then works both with int and str input
    if len(str_imo) == 7:
        try:
            il = int(str_imo[:-1])
        except ValueError:
            print("This imo seems invalid: {}".format(str_imo))
            continue
        try:
            ir = int(str_imo[-1:])
        except ValueError:
            print("This imo seems invalid: {}".format(str_imo))
            continue
        sl = str_imo[:-1]
        int_ctrl = (int(sl[0]) * 7
                    + int(sl[1]) * 6
                    + int(sl[2]) * 5
                    + int(sl[3]) * 4
                    + int(sl[4]) * 3
                    + int(sl[5]) * 2) % 10
        if ir != int_ctrl:
            print("Crazy: IMO number {} have ctrl cipher {}".format(str_imo, int_ctrl))
            continue  # Control number didn't check out, don't even try...
    else:
        print("Seems that IMO number is not 7 digits: |{}|".format(str_imo))
    cnt_good += 1
print("Valid: {} numbers".format(cnt_good))