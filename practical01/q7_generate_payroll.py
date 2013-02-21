# Filename: q7_generate_payroll.py
# Name: Ng Cheryl
# Created: 20130127
# Modified: 20130127
# Description: Program reads the following information:
# Name, no. of hours worked weekly, hourly pay rate, CPF contribution rate
# and prints a payroll statement

# main
while True:

# prompt and get name
    name = str(input("\nPlease enter your name: "))

# prompt and get no. of hours worked weekly
    hours = int(input("Please enter the number of hours worked weekly: "))

# prompt and get hourly pay rate
    pay_rate = float(input("Please enter your hourly pay rate: "))

# prompt and get CPF contribution rate
    cpf_rate = float(input("Please enter your CPF contribution rate in %: "))

# calculate gross pay
    gross_pay = hours*pay_rate

# calculate CPF contribution
    cpf = cpf_rate/100*gross_pay

# calculate net pay
    net_pay = gross_pay - cpf

# display result
    print ("\nPayroll statement for " + name)
    print ("Number of hours worked in week: " + str(hours))
    print ("Hourly pay rate: ${0:.2f}".format(pay_rate))
    print ("Gross pay = ${0:.2f}".format(gross_pay))
    print ("CPF contribution at {0:.2f}".format(cpf_rate) + "% = ${0:.2f}".format(cpf))
    print ("Net pay = ${0:.2f}".format(net_pay))

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
