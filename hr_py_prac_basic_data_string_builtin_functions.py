if __name__ == '__main__':
    s = raw_input()
    ls=list(s)
    falnum=falpha=fdigit=flower=fupper=0
    for i in ls:
        if i.isalnum():
            falnum=1
            break
    for i in ls:
        if i.isalpha():
            falpha=1
            break
    for i in ls:
        if i.isdigit():
            fdigit=1
            break
    for i in ls:
        if i.islower():
            flower=1
            break
    for i in ls:
        if i.isupper():
            fupper=1
            break 
    if falnum:
        print True
    else:
        print False
    if falpha:
        print True
    else:
        print False
    if fdigit:
        print True
    else:
        print False
    if flower:
        print True
    else:
        print False
    if fupper:
        print True
    else:
        print False
