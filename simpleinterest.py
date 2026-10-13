import sys

def simpInt(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "_main_":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    print("Simple interest: ", simpInt(p, i, t))


