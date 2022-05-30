import random
up=int(input('upper linit : '))
low=int(input('lower limit : '))
status='nothing yet'
innings=1
def toss1():
    var=input("heads or tails")
    res=random.choice(['heads','tails'])
    if(var==res):
        print(f'you win thw toss result is {var}')
        return makechoice()
    else:
        print(f'result is{var}, computer wins')
        if(random.choice(['bat','ball'])=='bat'):
            return userball()
        else:
            return userbat()

def varin():
    var=int(input("enter count"))
    while(True):
        if(var>up or var<low):
            var=int(input('out of range \n enter again'))
        break
    return var

def toss2():
   choice=input('odd or even')
   var=varin()
   comp=random.randint(low,up)
   print(f'your count==>{var}||{comp}<==computer\'s count')
   if((var+comp)%2==0):
        if(choice=='even'):
            print('you win the toss,even')
            print("===================================================")
            return makechoice()
        else:
            print('result is odd, computer wins')
            print("===================================================")
            if(random.choice(['bat','ball'])=='bat'):
                return userball()
            else:
                return userbat()
   else:
        if(choice=='odd'):
            print('you win the toss,odd')
            print("===================================================")
            return makechoice()
        else:
            print('result is even, computer wins')
            print("===================================================")
            if(random.choice(['bat','ball'])=='bat'):
                return userball()
            else:
                return userbat()

def makechoice():
    choice=input('bat or ball?')
    print("===================================================")
    if(choice=='bat'):
        return userbat()
    else:
        return userball()

def userbat():
    global status
    status='userbat'
    print('you are batting now')
    target=0
    while True:
        var=varin()
        
        comp=random.randint(low,up)
        print(f'your count==>{var}||{comp}<==computer\'s count')
        if(var!=comp):
            target+=var
            print('current score= ',target)
            print("===================================================")
        else:
            return target

def userbat2(score):
    global status
    status='userbat'
    print('you are batting now')
    while True:
        var=varin()
        target=0
        comp=random.randint(low,up)
        print(f'your count==>{var}||{comp}<==computer\'s count')
        if(var!=comp):
            target+=var
            print('current score= ',target)
            print("===================================================")
            if(score<target):
                return target
        else:
            return target

def userball():
    global status
    status='userball'
    print('you are balling now')
    target=0
    while True:
        var=varin()
        comp=random.randint(low,up)
        print(f'your count==>{var}||{comp}<==computer\'s count')
        if(var!=comp):
            target+=comp
            print('current score= ',target)
            print("===================================================")
        else:
            return target

def userball2(score):
    
    global status
    status='userball'
    print('you are balling now')
    target=0
    while True:
        var=varin()
        comp=random.randint(low,up)
        print(f'your count==>{var}||{comp}<==computer\'s count')
        if(var!=comp):
            target+=comp
            print('current score= ',target)
            print("===================================================")
            if(target>score):
                return target
        else:
            return target


def main():
    tosstype=input('toss1 or toss2')
    global status

    if tosstype=='toss1': var=toss1()
    else:
        var =toss2()
        
    print("status is ",status)
    if(status=='userbat'):
        print("===================================================")
        print('out! the user was bolt at ',var)
        print("===================================================")
        status='userball'
        var2=userball2(var)
        print("===================================================")
        print("out!the computer was bolt at ",var2)
        print("===================================================")
        if var>var2:
            print('current score= ',var2)
            print('user wins by',(var-var2))
            print("===================================================")
        elif var<var2:
            print('current score= ',var2)
            print('system wins by',(var2-var))
            print("===================================================")
        else:
            print('current score= ',var2)
            print('it\'s a tie')
            print("===================================================")
    else:
        print("===================================================")
        print('out! the system was bolt at ',var)
        print("===================================================")
        status='userbat'
        var2=userbat2(var)
        print("===================================================")
        print("out!the user was bolt at ",var2)
        print("===================================================")
        if var>var2:
            print('current score= ',var2)
            print('system wins by',(var-var2))
            print("===================================================")
        elif var<var2:
            print('current score= ',var2)
            print('user wins by',(var2-var))
            print("===================================================")
        else:
            print('current score= ',var2)
            print('it\'s a tie')
            print("===================================================")

def new_func():
    status2=status
    return status2
main()
            


    