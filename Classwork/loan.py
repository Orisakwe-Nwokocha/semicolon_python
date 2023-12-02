def emi(loan_amount, no_of_years, interest_rate):
    interest_rate = interest_rate / (12 * 100)
    no_of_months = no_of_years * 12
    
    # return monthly EMI, total payment and display the amortization schedule for the loan
    emi = (loan_amount * interest_rate * (1 + interest_rate) ** no_of_months) / ((1 + interest_rate) ** no_of_months - 1)
    total_payment = emi * no_of_months

    # display the amortization 
    amortization_schedule = []
    while no_of_months > 0:
        interest = loan_amount * interest_rate
        principal = emi - interest
        loan_amount = loan_amount - principal
        print(f"Interest: {interest:.2f}, Principal: {principal:.2f}, Loan Amount: {loan_amount:.2f}")
        no_of_months -= 1
    
    return emi, total_payment

if __name__ == "__main__":
    loan_amount = float(input("Enter the loan amount: "))
    no_of_years = float(input("Enter the number of years: "))
    interest_rate = float(input("Enter the interest rate: "))
    emi, total_payment = emi(loan_amount, no_of_years, interest_rate)
    print("Monthly EMI: ", emi)
    print("Total payment: ", total_payment)