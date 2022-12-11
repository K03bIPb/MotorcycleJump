import math
import random


def jump_again (T2, T3):
    A = input("WANT TO JUMP AGAIN")
    print()
    if A[-1:] == "Y" or A == "y":
        loop()
    if A[-1:] == "n" or A == "no":
        print(f"YOU MADE IT {T2} OUT OF {T3} ATTEMPTS.")
        print("BE CAREFUL, NOW.")


def loop():
    I2 = [-1] * 84
    I = "R.ARM L.ARM R.LEG L.LEG BACK NECK SKULL RIBS KNEE BUTT"
    print("MOTORCYCLE JUMP")
    print("CREATIVE COMPUTING")
    print("MORRISTOWN, NEW JERSEY")

    print("WE'RE AT THE SCENE OF THE BIG MOTORCYCLE JUMP!")
    print("HOW MANY BUSSES WILL YOU TRY TO JUMP")

    T = 0.1
    T2 = 0
    T3 = 0
    N = int(input())
    J = N * 15
    print(f" BUSSES!  THAT'S {J} FEET!")
    print("WHAT RAMP ANGLE WILL YOU USE")
    A2 = int(input())
    while not 0 < A2 < 90:
        print(f"{A2} DEGREES? THAT'S IMPOSSIBLE.  COME ON NOW, ")
        A2 = int(input())
    A = A2 * 0.01745
    print("HOW FAST WILL YOU LEAVE THE RAMP")
    S = int(input())
    print("GOOD LUCK!")
    while not S > 0:
        print("A PRACTICE JUMP!")
        print("OK, THIS TIME")
        S = int(input())
    H = 6
    D = 0
    G = 6
    R2 = 0
    S2 = 0
    S = S * 1.5
    print("THERE HE GOES!!!!")
    S = S - S2
    F = S * T
    D2 = F * math.cos(A)
    R = F * math.sin(A)
    R2 = R2 + (32 * T)
    R3 = R2 * T
    H = H + R - R3
    D = D + D2
    print("*")
    S2 = (S / 120) * 32 * T
    if D >= J:
        G = G - R
    if G <= R:
        G = 0
    while not H > G:
        S = S - S2
        F = S * T
        D2 = F * math.cos(A)
        R = F * math.sin(A)
        R2 = R2 + (32 * T)
        R3 = R2 * T
        H = H + R - R3
        D = D + D2
        print("*")
        print("G: ", G)
        print("H: ", H)
        print()
        S2 = (S / 120) * 32 * T
        if D >= J:
            G = G - R
        if G <= R:
            G = 0

    if not D < G:
        if not D > J + 20:
            L = ((D - J) / 30) + random.random()
            if not L > .8:
                print("HE MADE IT !  GREAT JUMP, KILLER!")
                T3 = T3 + 1
                T2 = T2 + 1
                jump_again(T2, T3)
                return 0
            else:
                print("HE MISSED THE RAMP.")
        else:
            print("HE JUMPED TOO FAR!")
            print("HE MISSED THE RAMP.")

    else:
        print("HE'S SHORT OF THE RAMP .....")
        print("I THINK HE'S HURT......")

    L2 = int((((J - D) / 5) * 2) + (random.random() * 5) + .5)
    for i in range(1, 14):
        I2[i] = i

    K2 = 14
    if L2 > 14:
        L2 = 14
    if L2 <= 0:
        L2 = 1

    for K in range(1, L2):
        V = int(random.random() * 1000)
        V = (V - (int(V / K2) * K2)) + 1
        H2 = I2[V]
        I2[V] = I2[K2]
        K2 = K2 - 1

    print("WELL, KILLER, THE DOCTOR SAYS YOU BROKE YOUR:")

    for K in range(4):
        A = I.split()
        print(A[random.randint(0, 9)])

    T3 = T3 + 1
    jump_again(T2, T3)


loop()
