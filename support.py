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

def menu(title, *options):
    count = 1
    for option in options:
        print(f"\033[34m{count}\033[m - \033[33m{option}\033[m")
        count +=1
    print()
    resp = verify_int(input("Please choose an option: "), range(1, count+1))
    return resp
