
# Credits:
# Budget Planner Tab : Karim Shawki
# Saving Calculator Tab : Fares Tamer
# Design and Layout : Ziad El Zeiny
# Planning and Management : Adam Roua (Joker helped everyone who needed help)
# Integration and Tabs Combining : Yassin Karim (Final Project Came from here)


import streamlit as st

# Config by : Yassin Karim

st.set_page_config(
    page_title="Budget Bunny",
    page_icon="🐰",
    layout="wide"
)

st.title("🐰 Budget Bunny")
st.subheader("Your simple household financial planner")

st.info("Plan your monthly expenses, manage your savings, and stay in control of your money!")

st.divider()



if "budget_result" not in st.session_state:
    st.session_state.budget_result = None

if "savings_result" not in st.session_state:
    st.session_state.savings_result = None



# TABS by : Yassin Karim


budget_tab, savings_tab = st.tabs([
    "💰 Monthly Budget Planner",
    "🎯 Savings Goal Calculator"
])



# TAB 1 Budget Planner By: Karim Shawki


with budget_tab:

    st.header("💰 Monthly Budget Planner", divider="green")
    st.write("Plan your household's monthly income and expenses for four people.")


    income = st.number_input(
        "Enter total household monthly income (EGP):",
        min_value=0,
        value=35000,
        step=1000,
        key="budget_income"
    )

    st.divider()

    st.subheader("Plan Your Monthly Expenses")


    col1, col2, col3 = st.columns(3)

    with col1:
        food = st.number_input(
            "Food Budget (EGP):",
            min_value=0,
            value=10000,
            step=500,
            key="food"
        )

        transport = st.number_input(
            "Transportation Budget (EGP):",
            min_value=0,
            value=6000,
            step=500,
            key="transport"
        )

    with col2:
        education = st.number_input(
            "Education Budget (EGP):",
            min_value=0,
            value=8000,
            step=500,
            key="education"
        )

        entertainment = st.number_input(
            "Entertainment Budget (EGP):",
            min_value=0,
            value=3000,
            step=500,
            key="entertainment"
        )

    with col3:
        shopping = st.number_input(
            "Shopping Budget (EGP):",
            min_value=0,
            value=4000,
            step=500,
            key="shopping"
        )

        other = st.number_input(
            "Other Expenses (EGP):",
            min_value=0,
            value=2000,
            step=500,
            key="other"
        )


    if st.button(
        "Calculate My Budget",
        type="primary",
        use_container_width=True,
        key="calculate_budget"
    ):

        total_expenses = (
            food
            + transport
            + education
            + entertainment
            + shopping
            + other
        )

        remaining_balance = income - total_expenses


        st.session_state.budget_result = {
            "income": income,
            "expenses": total_expenses,
            "balance": remaining_balance
        }


    if st.session_state.budget_result is not None:

        result = st.session_state.budget_result

        st.divider()
        st.subheader("Your Monthly Budget Results", divider="green")

        m1, m2, m3 = st.columns(3, gap="large")

        m1.metric(
            label="Monthly Income",
            value=f"{result['income']:,} EGP",
            border=True
        )

        m2.metric(
            label="Planned Expenses",
            value=f"{result['expenses']:,} EGP",
            border=True
        )

        m3.metric(
            label="Remaining Balance",
            value=f"{result['balance']:,} EGP",
            border=True
        )


        if result["balance"] > 0:
            st.success(
                "Great! Your household has money left to save."
            )

        elif result["balance"] == 0:
            st.warning(
                "Careful! You have used your entire monthly income."
            )

        else:
            st.error(
                f"Over budget! Your planned expenses exceed your income by "
                f"{abs(result['balance']):,} EGP."
            )



# TAB 2 Saving Calculator By: Fares Tamer


with savings_tab:

    st.header("🎯 Savings Goal Calculator", divider="blue")

    st.write(
        "Planning to buy a new phone, a bicycle, or pay for a course? "
        "Enter your goal details below to find out how long it will take."
    )

    
    goal_name = st.text_input(
        "What are you saving for?",
        placeholder="e.g., New Phone, Bicycle, Laptop",
        key="goal_name"
    )

   
    col1, col2 = st.columns(2)

    with col1:
        target_amount = st.number_input(
            "Target Amount (EGP)",
            min_value=0.0,
            step=100.0,
            format="%.2f",
            key="target_amount"
        )

    with col2:
        monthly_saving = st.number_input(
            "Monthly Saving Amount (EGP)",
            min_value=0.0,
            step=50.0,
            format="%.2f",
            key="monthly_saving"
        )

    
    if st.button(
        "Calculate My Savings Plan",
        type="primary",
        use_container_width=True,
        key="calculate_savings"
    ):

        if not goal_name.strip():
            st.warning(
                "⚠️ Please enter a Goal Name to continue."
            )

        elif target_amount <= 0:
            st.warning(
                "⚠️ Please enter a Target Amount greater than 0 EGP."
            )

        elif monthly_saving <= 0:
            st.warning(
                "⚠️ Please enter a Monthly Saving Amount greater than 0 EGP."
            )

        else:

            
            months_needed = int(target_amount / monthly_saving)

            if target_amount % monthly_saving != 0:
                months_needed += 1

            total_saved = months_needed * monthly_saving

            
            st.session_state.savings_result = {
                "goal": goal_name.strip(),
                "target": target_amount,
                "monthly": monthly_saving,
                "months": months_needed,
                "total": total_saved
            }

    
    if st.session_state.savings_result is not None:

        result = st.session_state.savings_result

        st.divider()

        st.subheader(
            f"Savings Plan for: {result['goal']}",
            divider="blue"
        )

        m1, m2, m3 = st.columns(3, gap="large")

        m1.metric(
            label="Target Amount",
            value=f"{result['target']:,.2f} EGP",
            border=True
        )

        m2.metric(
            label="Monthly Saving",
            value=f"{result['monthly']:,.2f} EGP",
            border=True
        )

        m3.metric(
            label="Estimated Time",
            value=f"{result['months']} "
            f"{'Month' if result['months'] == 1 else 'Months'}",
            border=True
        )

       
        st.success(
            f"🎉 Great plan! By saving "
            f"*{result['monthly']:,.2f} EGP* each month, "
            f"you will reach your *{result['target']:,.2f} EGP* "
            f"goal for *{result['goal']}* in "
            f"**{result['months']} "
            f"{'month' if result['months'] == 1 else 'months'}** "
            f"(total saved: *{result['total']:,.2f} EGP*)."
        )



# FOOTER


st.divider()

st.caption(
    "🐰 Budget Bunny | Making every pound count, one goal at a time."
)
