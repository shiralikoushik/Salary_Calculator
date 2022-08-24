
def _80_C(emp_pf):
    life_insurance = int(input("Enter Total life Insurance Premium: "))
    elss = int(input("Enter the amount paid to mutual funds: "))
    ppf = int(input("Enter the amount paid to PPF: "))
    nps = int(input("Enter the amount paid to NPS: "))

    if life_insurance+elss+ppf+emp_pf >= 150000:
        return 150000,nps
    elif life_insurance+elss+ppf+nps+emp_pf > 150000:
        return 150000,(life_insurance+elss+ppf+nps+emp_pf-150000)
    else:
        return (life_insurance+elss+ppf+nps+emp_pf),0
def _80_D(NPS):
    health_insurance = int(input("Enter Total Health Insurance Premium: "))
    other_medical = int(input("Enter other medical treatment expense: "))
    if NPS == 0:
        return health_insurance+other_medical
    elif NPS > 50000:
        return health_insurance+other_medical+50000
    else:
        return health_insurance+other_medical+NPS

def HRA(hra,base_sal):
    actual_amount_claimed = int(input("Enter the acutal amount claimed as HRA: "))
    return min(hra/12,actual_amount_claimed - (0.1*(base_sal/12)),0.4*(base_sal/12))

def user_input():
    ctc = int(input("Enter the ctc amount: "))
    base_sal = int(input("Enter the base salary: "))
    hra = int(input("Enter the HRA amount given by the company: "))
    allowance = int(input("Enter the other allowance given by the company: "))
    comp_pf = int(input("Enter the pf given by the company: "))
    return ctc,base_sal,hra,allowance,comp_pf

def cal_salary():
    pass
ctc,base_sal,hra,allowance,comp_pf = user_input()
hra_final = HRA(hra,base_sal)
print ("Total excemption for HRA is {} per annum or {} per month".format(hra_final*12,hra_final))
_80c,nps = _80_C(comp_pf)
print(_80c,nps)
_80d = _80_D(nps)
print(_80d)