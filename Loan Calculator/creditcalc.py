import argparse
import sys
import math

type_val = ""
payment_val = 0
principal_val = 0
periods_val = 0
interest_val = 0

def check_input_args():

    value = 1

    global type_val, payment_val, principal_val, periods_val, interest_val

    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--payment", default=0)
    parser.add_argument("--principal", default=0)
    parser.add_argument("--periods", default=0)
    parser.add_argument("--interest", default=0)

    args = parser.parse_args()

    type_val      = str(args.type)
    payment_val   = int(args.payment)
    principal_val = args.principal
    periods_val   = int(args.periods)
    interest_val  = float(args.interest)

    if type_val != "annuity" and type_val != "diff":
        value = -1

    if payment_val < 0 or (payment_val >0 and type_val == "diff"):
        value = -1

    if interest_val == "" or (interest_val  < 0):
        value = -1

    if payment_val < 0:
        value = -1

    if periods_val < 0:
        value = -1

    if len(sys.argv) != 5:
        value = -1

    return value

def calcDiffPmt(principal, periods, interest):
    # --type = diff - -principal = 1000000 - -periods = 10 - -interest = 10

    pmt_sum = 0
    pmt_monthly = 0

    loan_principal = int(principal)
    number_of_periods = int(periods)
    loan_interest = float(interest)

    int_ln = (loan_interest / 100) / 12

    for i in range(1, number_of_periods+1):

        pmt_monthly = (loan_principal / number_of_periods) + (int_ln * (loan_principal - (loan_principal*(i-1))/number_of_periods))
        pmt_sum += math.ceil(pmt_monthly)
        print("Month " + str(i) + ": payment is " + str(math.ceil(pmt_monthly)))

    print("Overpayment = " + str(int(pmt_sum) - loan_principal))

    return

def calcAnnuityPmt(principal, periods, interest):
    # --type=annuity --principal=1000000 --periods=60 --interest=10

    loan_principal = int(principal)
    number_of_periods = int(periods)
    loan_interest = float(interest)

    i = (loan_interest / 100) / 12
    n = number_of_periods
    P = loan_principal

    annuity = int(math.ceil(P * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))))

    print("Your annuity payment = " + str(annuity) + "!")

    overpayment = (annuity * number_of_periods) - loan_principal
    print("Overpayment = " + str(overpayment))

    return

def calcPrincipial(payment, periods, interest):
    # --type=annuity --payment=8722 --periods=120 --interest=5.6

    annuity_payment = float(payment)
    number_of_periods = int(periods)
    loan_interest = float(interest)

    i = (loan_interest / 100) / 12
    A = annuity_payment
    P = A / ((i * math.pow(1 + i, number_of_periods)) / (math.pow(1 + i, number_of_periods) - 1))

    print("Your loan principal = " + str(int(P)) + "!")
    print("Overpayment = " + str(int(math.ceil((annuity_payment * number_of_periods) - P))))

    return

def calcRepayLoan(principal, payment, interest):
    # --type=annuity --principal=500000 --payment=23000 --interest=7.8

    loan_principal = int(principal)
    monthly_payment = int(payment)
    loan_interest = float(interest)

    i = (loan_interest / 100) / 12
    A = monthly_payment
    P = loan_principal
    n = math.ceil(math.log((A / (A - i * P)), 1 + i))

    years = (int)(n / 12)
    months = n - years * 12

    if years == 0:
        print("It will " + str(months) + " months to repay this loan!")
    elif years == 1:
        if months == 0:
            print("It will take 1 year to repay this loan!")
        else:
            print("It will take 1 year and " + str(months) + " months to repay this loan!")
    else:
        if months == 0:
            print("It will take " + str(years) + " years to repay this loan!")
        else:
            print("It will take " + str(years) + " years and " + str(months) + " months to repay this loan!")

    overpayment = (monthly_payment * n) - loan_principal
    print("Overpayment = " + str(overpayment))

    return


if check_input_args() != 1:

    print("Incorrect parameters")
else:

    if type_val == "diff":

        if int(principal_val) > 0 and int(periods_val) > 0 and float(interest_val) > 0:
            calcDiffPmt(principal_val, periods_val, interest_val)

    if type_val == "annuity":

        if int(principal_val) > 0 and int(periods_val) > 0 and float(interest_val) > 0:
            calcAnnuityPmt(principal_val, periods_val, interest_val)

        if int(payment_val) > 0 and int(periods_val) > 0 and float(interest_val) > 0:
            calcPrincipial(payment_val, periods_val, interest_val)

        if int(principal_val) > 0 and int(payment_val) > 0 and float(interest_val) > 0:
            calcRepayLoan(principal_val, payment_val, interest_val)

