import sys

def simInt(principal, interest, time):
    return (principal * interest * time) / 100

if _name_ == "_main_":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    print("Simple interest: ", simInt(p, i, t))


