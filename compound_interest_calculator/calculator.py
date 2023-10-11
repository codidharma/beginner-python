print('Welcome to the compound interest calculator.')
principal = float(input('Enter the principal amount: '))
rate_of_interest_per_annum = float(input('Enter the rate of interest per annum: '))
number_of_years = int(input('Enter the number of years for which the principal will be compounded: '))

total_amount = principal * ((1+(rate_of_interest_per_annum/ 100))
                             ** number_of_years)

compound_interest = total_amount - principal
print('Total amount after compounding is ' + str(total_amount))
print('Compound interest is ' + str(compound_interest))
print(f'''The total amount is {total_amount:0.3f}
      The compound interest is {compound_interest:0.3f}''')