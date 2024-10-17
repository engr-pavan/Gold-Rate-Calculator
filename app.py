import streamlit as st

# Function to calculate the total gold price based on karat and weight in tola
def calculate_gold_price(weight_in_tola, rate_per_tola, purity_percentage):
    pure_gold_rate = rate_per_tola * (purity_percentage / 100)
    return weight_in_tola * pure_gold_rate

# Dictionary for purity percentages of different gold karats
karat_purity = {
    '24K': 100,        # 100% pure
    '22K': 91.67,      # 91.67% pure
    '21K': 87.5,       # 87.5% pure
    '20K': 83.33,      # 83.33% pure
    '19K': 79.17,      # 79.17% pure
    '18K': 75          # 75% pure
}

# Currency exchange rates (example values, you'd need to update them based on live rates)
currency_rates = {
    'PKR': 1,          # Base currency (e.g., Pakistani Rupees)
    'USD': 280,        # 1 USD = 280 PKR (example rate)
    'EUR': 300,        # 1 EUR = 300 PKR (example rate)
    # Add other currencies if needed
}

# Streamlit user interface
st.title('Gold Rate Calculator')

# Input fields
weight_in_tola = st.number_input("Enter the weight of gold (in tolas): ", min_value=0.0, value=1.0)
gold_karat = st.selectbox("Select the gold purity (Karat): ", options=['24K', '22K', '21K', '20K', '19K', '18K'])
rate_per_tola = st.number_input(f"Enter the current rate of 24K gold per tola in your base currency: ", min_value=0.0, value=200000.0)
currency = st.selectbox("Select the currency: ", options=['PKR', 'USD', 'EUR'])

# Convert the rate to PKR if another currency is selected
if currency != 'PKR':
    rate_per_tola *= currency_rates[currency]

# Get the purity percentage based on the karat
purity_percentage = karat_purity.get(gold_karat, 100)

# Calculate the total cost when the user presses the button
if st.button('Calculate'):
    total_cost = calculate_gold_price(weight_in_tola, rate_per_tola, purity_percentage)
    st.write(f"The total cost of {weight_in_tola} tolas of {gold_karat} gold is: {total_cost:.2f} PKR")

