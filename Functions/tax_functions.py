def get_soc_sec_tax(gross_pay):
    tax_rate = 0.062
    return gross_pay * tax_rate

def get_medicare_tax(gross_pay):
    tax_rate = 0.0145
    return gross_pay * tax_rate

def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        tax_rate = 0.23
    elif withholding_code == 1:
        tax_rate = 0.21
    elif withholding_code == 2:
        tax_rate = 0.195
    elif withholding_code == 3:
        tax_rate = 0.185
    elif withholding_code >= 4:
        tax_rate = 0.18 - ((withholding_code - 4) * 0.005)
    return gross_pay * tax_rate

person1 = {"gross_pay": 750, "withholding_code": 0}
person2 = {"gross_pay": 1550, "withholding_code": 2}
person3 = {"gross_pay": 1100, "withholding_code": 5}

for i, person in enumerate([person1, person2, person3], start=1):
    gross_pay = person["gross_pay"]
    withholding_code = person["withholding_code"]
    
    soc_sec_tax = get_soc_sec_tax(gross_pay)
    medicare_tax = get_medicare_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay, withholding_code)
    
    print(f"Person {i}:")
    print(f"Gross Pay: ${gross_pay}")
    print(f"Social Security Tax: ${soc_sec_tax:.2f}")
    print(f"Medicare Tax: ${medicare_tax:.2f}")
    print(f"Federal Tax: ${federal_tax:.2f}")
    print("\n")