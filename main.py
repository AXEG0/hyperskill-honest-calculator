msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def read_calc():
    print(msg_0)
    un = input()
    return un

def split_calc():
    myString = un
    a = myString.split()
    firstName, lastName, Hey = a[0], a[1], a[2]
    return firstName, lastName, Hey

def what_is_memory(var):
    if var == "M":
        return True
    else:
        return False

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return True
        except ValueError:
            print(msg_1)
            return False

def check_oper_input(sign):
    if sign not in {"+", "-", "*", "/"}:
        print(msg_2)
        return False
    else:
        return True

def is_one_digit(v):
    if float(v) > -10 and float(v) < 10 and float(v).is_integer():
        return True
    else:
        return False

def dumb(x, oper, y):
    msg = ""
    if is_one_digit(x) and is_one_digit(y) == True:
        msg = msg + msg_6
    if (x == "1" or y == "1") and oper == "*":
        msg = msg+msg_7
    if (x == "0" or y == "0") and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)

def dev_zero(oper, y):
    if oper == "/" and y == "0":
        print(msg_3)
        return False

def sum(x, oper, y):
    if oper == "+":
        return float(x) + float(y)
    if oper == "-":
        return float(x) - float(y)
    if oper == "*":
        return float(x) * float(y)
    if oper == "/":
        return float(x) / float(y)

def remember_or_not():
    print(msg_4)
    res = input()
    if res == "y":
        return True
    else:
        return False

def want_more():
    print(msg_5)
    res = input()
    if res == "y":
        return True
    else:
        return False

def saving_memory():
    msg_index = 10
    while True:
        if msg_index == 10:
            print(msg_10)
        elif msg_index == 11:
            print(msg_11)
        elif msg_index == 12:
            print(msg_12)
        elif msg_index == 13:
            return True
            break
        answer = input()
        if answer == "n":
            return False
            break
        if answer == "y" and msg_index <= 12:
            msg_index += 1
            continue


l=[]

while True:

    if l != []:
        memory = l[-1]
    else:
        memory = "0"

    un = read_calc()
    un_1, un_2, un_3 = split_calc()

    if what_is_memory(un_1) == True:
        un_1 = memory
    if what_is_memory(un_3) == True:
        un_3 = memory

    if check_user_input(un_1) == False:
        continue
    elif check_oper_input(un_2) ==  False:
        continue
    elif check_user_input(un_3) ==  False:
        continue

    dumb(un_1, un_2, un_3)

    if dev_zero(un_2, un_3) == False:
        continue
    else:
        result = sum(un_1, un_2, un_3)
        print(result)

    if remember_or_not() == True and is_one_digit(result) == True:
        if saving_memory() == True:
            l.append(result)
    elif is_one_digit(result) == False:
        l.append(result)
    if want_more() == True:
        continue
    break


