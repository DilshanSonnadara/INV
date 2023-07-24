import streamlit as st

def calculate_return_with_tax(interest_rate, tax_rate, years, annual_investment):
    total_amount = 0

    for i in range(years):
        interest = (total_amount + annual_investment) * interest_rate
        interest_after_tax = interest * (1 - tax_rate)
        total_amount += annual_investment + interest_after_tax
    
    return total_amount

st.title('Investment Calculator')

st.write('Calculate your returns over time considering interest rate, tax rate, investment period, and annual investment amount.')

interest_rate = st.slider('Enter the annual interest rate (as a decimal)', min_value=0.0, max_value=1.0, value=0.1, step=0.01)
tax_rate = st.slider('Enter the tax rate (as a decimal)', min_value=0.0, max_value=1.0, value=0.05, step=0.01)
years = st.slider('Enter the number of years', min_value=1, max_value=50, value=20, step=1)
annual_investment = st.slider('Enter the annual investment amount', min_value=1000, max_value=100000, value=86000, step=1000)

if st.button('Calculate Return'):
    result = calculate_return_with_tax(interest_rate, tax_rate, years, annual_investment)
    st.success(f'The return after {years} years will be: ${result:,.2f}')

st.write('---')
st.write('Product of Quantum-AI')
