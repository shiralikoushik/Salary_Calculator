def min_hra(basic,hra,rent):
    cal_1 = rent - (0.1*basic/12)
    cal_2 = 0.4 * basic/12

    return(min(cal_1,cal_2,(hra/12)))

basic = int(input("Enter your basic amount per annum: "))
hra = int(input("Enter the HRA given by the company per annum: "))
rent = int(input("Enter the rent amount per month:  "))

hra_ex = min_hra(basic,hra,rent)
print(f"The max HR excemption you will get is {hra_ex}")