def rep_char(c, n):
    print(c * n)

def welcome_msg(name):
    msg1='Hello '+ name
    msg2='Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr + 2)
    print(f' {msg1},\n {msg2} ')
    rep_char('-', nstr + 2)

name=input('Input his/her name:')
print(name)
welcome_msg(name)