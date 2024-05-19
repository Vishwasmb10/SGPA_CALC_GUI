def Calc(credit,grade,n):
    SGPA=0
    Sum=0
    for i in range(n):
        Sum+=(credit[i]*grade[i])
    SGPA=Sum/sum(credit)
    return SGPA