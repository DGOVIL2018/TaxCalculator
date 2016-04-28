#Dhruv Govil Period 2 April 6 2016
#Lab 1 -- Tax Calculator and Individualized Tax Plan


def taxCalc(income,a1,b1,b2,b3,b4,b5,t1,t2,t3,t4,t5,t6): #takes income and tax table parameters and returns taxes

    taxableIncome = income - 9500

    if taxableIncome < a1:
        TX = 0
    elif taxableIncome <= b1:
        TX = taxableIncome*t1/100
    elif taxableIncome <= b2:
        TX = (taxableIncome - b1)*(t2/100) + b1*t1/100
    elif taxableIncome <= b3:
        TX = (taxableIncome - b2)*t3/100 + (b2 - b1)*t2/100 + (b1 - a1)*t1/100
    elif taxableIncome <= b4:
        TX = (taxableIncome - b3)*t4/100 + (b3 - b2)*t3/100 + (b2 - b1)*t2/100 + (b1 - a1)*t1/100
    elif taxableIncome <= b5:
        TX = (taxableIncome - b4)*t5/100 + (b4 - b3)*t4/100 + (b3 - b2)*t3/100 + (b2 - b1)*t2/10 + (b1 - a1)*t1/ 100                                                                    
    elif taxableIncome > b5:
        TX = (taxableIncome - b5)*t6/100 + (b5 - b4)*t5/100 + (b4 - b3)*t4/100 + (b3 - b2)*t3/100 + (b2 - b1)*t2/100 + (b1-a1)*t1/100                                                                           
    return TX                                                                           
            
def Clinton_TaxPlan_2000(income): #sets the Clinton tax table parameters and calls taxCalc with them
    a1=0
    b1=2650 
    b2=27850
    b3=59900
    b4=134200
    b5=289950
    t1=0
    t2=15
    t3=28
    t4=31
    t5=36
    t6=39.6
    return taxCalc(income,a1,b1,b2,b3,b4,b5,t1,t2,t3,t4,t5,t6)
                                                                       

def Bush_TaxPlan_2008(income): #sets the Bush tax table parameters and calls taxCalc with them
    a1=0
    b1=8025 
    b2=32550
    b3=78850
    b4=164550
    b5=357700
    t1=10
    t2=15
    t3=25
    t4=28
    t5=33
    t6=35
    return taxCalc(income,a1,b1,b2,b3,b4,b5,t1,t2,t3,t4,t5,t6)
                                                    
    
def Obama_TaxPlan_2014(income): #sets the Obama tax table parameters and calls taxCalc with them
    a1=0
    b1=8700 
    b2=35350
    b3=85650
    b4=178650
    b5=388350
    t1=10
    t2=15
    t3=25
    t4=28
    t5=33
    t6=35
    return taxCalc(income,a1,b1,b2,b3,b4,b5,t1,t2,t3,t4,t5,t6)

  

### Main Program Begins #####

print("Welcome to the Tax Calculator.")
income = input("Enter your total income from last year: ")
income = float(income)


taxesClinton = Clinton_TaxPlan_2000(income)
taxesBush = Bush_TaxPlan_2008(income)
taxesObama = Obama_TaxPlan_2014(income)

if income <= 0:
    GIT_Clinton = 0
    GIT_Bush = 0
    GIT_Obama = 0
    
else:    
    GIT_Clinton = (taxesClinton / income)*100
    GIT_Bush = (taxesBush / income)*100
    GIT_Obama = (taxesObama / income)*100

NI_Clinton = income - taxesClinton
NI_Bush = income - taxesBush
NI_Obama = income - taxesObama

#print results

print()
print("Results for Clinton's plan.")
print("Taxes owed: $" , round(taxesClinton,2))
print("Percent of gross: " ,round(GIT_Clinton,2), "%")
print("Net income: $" , round(NI_Clinton,2))
print()

print("Results for Bush's plan.")
print("Taxes owed: $" , round(taxesBush,2))
print("Percent of gross: " ,round(GIT_Bush,2), "%")
print("Net income: $" , round(NI_Bush,2))
print()

print("Results for Obama's plan.")
print("Taxes owed: $" , round(taxesObama,2))
print("Percent of gross: " ,round(GIT_Obama,2), "%")
print("Net income: $" , round(NI_Obama,2))
print()

#print which tax plan is better for the user

if (NI_Clinton > NI_Bush) and (NI_Clinton > NI_Obama):
    print("The Clinton Tax Plan is the best for you, based on your gross income.")
if (NI_Bush > NI_Clinton) and (NI_Bush > NI_Obama):
    print("The Bush Tax Plan is the best for you, based on your gross income.")
if (NI_Obama > NI_Bush) and (NI_Obama > NI_Clinton):
    print("The Obama Tax Plan is the best for you, based on your gross income.")                                                                                                                                                                                                                                
