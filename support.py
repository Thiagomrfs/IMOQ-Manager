def msg(text, cor=""):
    print(f"\033[{cor}m"+"="*(len(text)+4))
    print(text.center(len(text)+4))
    print("="*(len(text)+4)+"\033[m")

def horizontal_line(len=10):
    print("="*len)

def verify_int(value, accepted):
    try:
        if int(value) in accepted:
            return int(value)
    except:
        while True:
            try:
                value = int(input("\033[31mPlease insert a valid value: \033[m"))
                if value in accepted:
                    return value
                    break
            except:
                pass
    return value

def verify_yes_no(resp):
    if resp.upper() in "YN" and resp != "":
        return resp.upper()
    else:
        while True:
            resp = input("\033[31mPlease insert a valid response [Y/N]: \033[m")
            if resp.upper() in "YN" and resp != "":
                return resp.upper()
                break

def menu(title, *options):
    count = 1
    for option in options:
        print(f"\033[34m{count}\033[m - \033[33m{option}\033[m")
        count +=1
    print()
    resp = verify_int(input("Please choose an option: "), range(1, count+1))
    return resp

def confirm_question(question):
    print("\n\033[31mAre these informations correct?\n\033[m")
    print("\033[34m" + question["question"] + "\033[34m")
    print("\033[33m")
    print("A) " + question["A"])
    print("B) " + question["B"])
    print("C) " + question["C"])
    print("D) " + question["D"])
    print("E) " + question["E"])
    print("\033[m")

    resp = verify_yes_no(input("Are you sure? "))
    return resp
