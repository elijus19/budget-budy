import streamlit as st

password = "Budget-budy2266!"
# 1. Simple Password Gate
def check_password():
    if "password_correct" not in st.session_state:
        st.text_input("Enter Password", type="password", on_change=lambda: st.session_state.update({"password_correct": st.session_state.password == password}), key="password")
        return False
    return st.session_state["password_correct"]

if not check_password():
    st.stop()  # Stop right here if password is wrong

# 2. Your Actual App Code Starts Here...
st.title("Our Budget 2026")
# ... the rest of your code ...


# --- APP CONFIG ---
st.set_page_config(page_title="Budget 2026", page_icon="📈", layout="centered")

# --- CUSTOM CSS FOR MOBILE ---
st.markdown("""
    <style>
    .main { max-width: 500px; margin: 0 auto; }
    .stCheckbox { font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- MASTER DATA STRUCTURE ---
# This mimics the "Template" you wanted.
months = ["April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = "2026"

# Default values from your screenshot
DEFAULT_BILLS = {
    "Rent": 550.00, "Car loan": 274.22, "Phone payment": 57.49,
    "Utility taxes": 200.00, "Internet": 40.00, "Car insurance": 71.95
}
DEFAULT_SUBS = {
    "Spotify": 10.99, "Youtube": 12.99, "Netflix": 15.99, 
    "Google workspace": 6.00, "Hostinger": 10.00, "Icloud": 0.99, "Go3": 7.00
}
DEFAULT_EXPENSES = {
    "Food": 400.00, "Car expenses": 400.00, "Stela beauty": 53.00, "Elijus haircut": 40.00
}

# --- THE LOGIC ---
st.title("💸 Finance Tracker 2026")

# Global Savings Goal ($12,000)
st.sidebar.header("🎯 Total Progress")
total_saved_all_months = 0.0 # This would pull from a database in reality

for month in months:
    # Use a unique key for each month's container
    with st.expander(f"📅 {month} {year}"):
        
        # 1. INCOME INPUTS
        col1, col2 = st.columns(2)
        with col1:
            elijus_inc = st.number_input(f"Elijus Income ({month})", value=1750.0, key=f"el_inc_{month}")
        with col2:
            stela_inc = st.number_input(f"Stela Income ({month})", value=1200.0, key=f"st_inc_{month}")
        
        income_total = elijus_inc + stela_inc
        spent_total = 0.0
        
        # 2. BILLS SECTION
        st.markdown("### 🏠 Bills")
        for name, amt in DEFAULT_BILLS.items():
            if st.checkbox(f"{name} (${amt})", key=f"bill_{name}_{month}"):
                spent_total += amt
                
        # 3. SUBSCRIPTIONS SECTION
        st.markdown("### 📺 Subscriptions")
        for name, amt in DEFAULT_SUBS.items():
            if st.checkbox(f"{name} (${amt})", key=f"sub_{name}_{month}"):
                spent_total += amt
                
        # 4. EXPENSES SECTION
        st.markdown("### 🛒 Expenses")
        for name, amt in DEFAULT_EXPENSES.items():
            if st.checkbox(f"{name} (${amt})", key=f"exp_{name}_{month}"):
                spent_total += amt

        # 5. SAVINGS (The $10k + $2k Goal)
        st.markdown("### 💰 Savings")
        saved_amt = st.number_input(f"Amount Saved to Goals ({month})", value=0.0, key=f"save_{month}")
        spent_total += saved_amt # We count savings as "spent" from checking
        
        # MONTHLY SUMMARY HEADER (Inside Expansion)
        remaining = income_total - spent_total
        
        st.divider
