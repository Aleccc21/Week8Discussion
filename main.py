#Initial input
annualized_interest_rate = float(input("Please enter your annualized interest rate in %: "))
initial_investment_amount = float(input("Please enter your initial investment amount: "))

#Program calculation
def calculation(initial_investment_amount, annualized_interest_rate):
  wanted_value = initial_investment_amount * 2
  current_value = initial_investment_amount
  years = 0

  while current_value < wanted_value:
    current_value += current_value * (annualized_interest_rate / 100)
    years += 1

  return years

#Final output
years_for_double = calculation(initial_investment_amount, annualized_interest_rate)
print(f"It will take you {years_for_double} years for your investment to double")
