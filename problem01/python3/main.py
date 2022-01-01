import numpy as np

SURVIVE=0.96
EMERGE=0.3
CLUTCH_PROP=1.2
TIME=100
INIT_LARVAL=100

if __name__ == "__main__":
    f = open("output", mode="w")
    S = SURVIVE
    E = EMERGE
    A = CLUTCH_PROP

    larval = INIT_LARVAL
    period = 10
    for t in range(1,TIME+1):
        adults = 0
        if t%period == 0:
            adults = int(E * larval)
            larval = 0
        larval = int(S*larval)
        larval += (adults//2) * int(A*period)
        f.write(f"{t} {larval}\n")
    f.close()