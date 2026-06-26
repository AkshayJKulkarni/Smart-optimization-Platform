import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from datetime import datetime

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Smart Inventory Optimization Platform",
    page_icon="🛒",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("catboost_inventory_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")
encoders = joblib.load("label_encoders.pkl")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🛒 Smart Inventory")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📦 Demand Forecast",
        "📊 Model Performance",
        "📈 Business Analytics",
        "ℹ️ About"
    ]
)

# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.title("🛒 AI-Driven Retail Intelligence & Smart Inventory Optimization Platform")

    st.markdown("""
### Intelligent Retail Inventory Management using Machine Learning

This platform predicts future product demand using **CatBoost Regression**
and provides inventory optimization recommendations to reduce
stock-outs and overstock situations.
""")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Dataset Size", "73,100")
    col2.metric("Best Model", "CatBoost")
    col3.metric("Best R²", "0.716")
    col4.metric("Models Evaluated", "4")

    st.divider()

    st.subheader("🎯 Project Objectives")

    c1, c2 = st.columns(2)

    with c1:
        st.success("""
✅ Predict future retail demand

✅ Optimize inventory

✅ Reduce stock shortages

✅ Reduce overstock

✅ Improve business decisions
""")

    with c2:
        st.info("""
Machine Learning Models

• Random Forest

• XGBoost

• CatBoost

• LSTM
""")

    st.divider()

    st.subheader("⚙ Technology Stack")

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
### Programming

- Python
- Pandas
- NumPy
""")

    with b:
        st.markdown("""
### Machine Learning

- CatBoost
- Random Forest
- XGBoost
- LSTM
""")

    with c:
        st.markdown("""
### Deployment

- Streamlit
- Plotly
- Joblib
- Google Colab
""")

# ============================================================
# DEMAND FORECAST PAGE
# ============================================================

elif page == "📦 Demand Forecast":

    st.title("📦 Demand Forecast & Inventory Optimization")

    # User Inputs
    store_id = st.selectbox("Store ID", ["S001", "S002", "S003", "S004", "S005"])

    product_id = st.selectbox(
        "Product ID",
        [f"P{str(i).zfill(4)}" for i in range(1, 21)]
    )

    category = st.selectbox(
        "Category",
        ["Groceries", "Toys", "Electronics", "Furniture", "Clothing"]
    )

    region = st.selectbox(
        "Region",
        ["North", "South", "East", "West"]
    )

    inventory_level = st.number_input(
        "Inventory Level",
        min_value=0,
        value=100
    )

    units_ordered = st.number_input(
        "Units Ordered",
        min_value=0,
        value=50
    )

    price = st.number_input(
        "Price",
        min_value=1.0,
        value=100.0
    )

    discount = st.slider(
        "Discount (%)",
        0,
        50,
        10
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Sunny", "Rainy", "Cloudy", "Snowy"]
    )

    holiday = st.selectbox(
        "Holiday / Promotion",
        [0, 1]
    )

    competitor_price = st.number_input(
        "Competitor Pricing",
        min_value=1.0,
        value=90.0
    )

    seasonality = st.selectbox(
        "Seasonality",
        ["Spring", "Summer", "Autumn", "Winter"]
    )

    previous_sales = st.number_input(
        "Previous Sales",
        min_value=0,
        value=120
    )

    rolling_sales_mean = st.number_input(
        "Rolling Sales Mean",
        min_value=0,
        value=110
    )

    if st.button("Predict Demand"):

        today = datetime.now()

        year = today.year
        month = today.month
        day = today.day
        dayofweek = today.weekday()
        isweekend = 1 if dayofweek >= 5 else 0

        price_comp_ratio = price / competitor_price

        discount_effect = price * (discount / 100)

        inventory_gap = inventory_level - rolling_sales_mean

        discount_comp_ratio = discount / competitor_price

        order_fulfillment_ratio = (
            inventory_level / units_ordered
            if units_ordered > 0 else 0
        )

        rolling_sales_mean7 = rolling_sales_mean

        rolling_sales_max7 = rolling_sales_mean * 1.1

        store_id = encoders["Store ID"].transform([store_id])[0]
        product_id = encoders["Product ID"].transform([product_id])[0]
        category = encoders["Category"].transform([category])[0]
        region = encoders["Region"].transform([region])[0]
        weather = encoders["Weather Condition"].transform([weather])[0]
        seasonality = encoders["Seasonality"].transform([seasonality])[0]

        input_df = pd.DataFrame([{
            'Store ID': store_id,
            'Product ID': product_id,
            'Category': category,
            'Region': region,
            'Inventory Level': inventory_level,
            'Units Ordered': units_ordered,
            'Price': price,
            'Discount': discount,
            'Weather Condition': weather,
            'Holiday/Promotion': holiday,
            'Competitor Pricing': competitor_price,
            'Seasonality': seasonality,
            'Year': year,
            'Month': month,
            'Day': day,
            'DayOfWeek': dayofweek,
            'IsWeekend': isweekend,
            'PriceCompetitorRatio': price_comp_ratio,
            'DiscountEffect': discount_effect,
            'PreviousSales': previous_sales,
            'RollingSalesMean': rolling_sales_mean,
            'InventoryGap': inventory_gap,
            'DiscountCompetitorRatio': discount_comp_ratio,
            'OrderFulfillmentRatio': order_fulfillment_ratio,
            'RollingSalesMean7': rolling_sales_mean7,
            'RollingSalesMax7': rolling_sales_max7
        }])

        # Match the feature order used during training
        input_df = input_df[feature_columns]

        prediction = model.predict(input_df)[0]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Current Inventory", inventory_level)

        with col2:
            st.metric("Predicted Demand", f"{prediction:.0f}")

        with col3:
            difference = prediction - inventory_level
            st.metric("Demand Gap", f"{difference:.0f}")

        if inventory_level < prediction:
            st.error("⚠️ UNDERSTOCK RISK")
            recommended_stock = prediction * 1.2
            reorder_qty = max(0, recommended_stock - inventory_level)
            st.write(f"Recommended Reorder Quantity: {reorder_qty:.0f}")

        elif inventory_level > prediction * 1.3:
            st.warning("📦 OVERSTOCK RISK")
            st.write("Reduce future procurement and run promotions.")

        else:
            st.success("✅ OPTIMAL INVENTORY LEVEL")

# ============================================================
# MODEL PERFORMANCE PAGE
# ============================================================

elif page == "📊 Model Performance":

    st.title("📊 Model Performance Dashboard")

    performance = pd.DataFrame({
        "Model": [
            "Random Forest",
            "XGBoost",
            "CatBoost",
            "LSTM"
        ],
        "R² Score": [
            0.715378,
            0.714981,
            0.716386,
            -0.001814
        ]
    })

    st.subheader("Model Comparison")

    st.dataframe(
        performance,
        use_container_width=True
    )

    fig = px.bar(
        performance,
        x="Model",
        y="R² Score",
        color="Model",
        text="R² Score",
        title="Model Performance Comparison"
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    best = performance.loc[
        performance["R² Score"].idxmax()
    ]

    st.success(
        f"""
🏆 Best Model

Model : {best['Model']}

R² Score : {best['R² Score']:.3f}
"""
    )

# ============================================================
# BUSINESS ANALYTICS PAGE
# ============================================================

elif page == "📈 Business Analytics":

    st.title("📈 Business Analytics")

    st.info(
        """
This dashboard provides business insights generated
from the trained Machine Learning model.
"""
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Dataset Size", "73,100")
    col2.metric("Products", "20")
    col3.metric("Stores", "5")

    st.divider()

    analytics = pd.DataFrame({
        "Metric": [
            "Best Model",
            "Highest R²",
            "Models Evaluated",
            "Deployment"
        ],
        "Value": [
            "CatBoost",
            "0.716",
            "4",
            "Streamlit"
        ]
    })

    st.dataframe(
        analytics,
        use_container_width=True
    )

    st.success(
"""
Business Benefits

• Reduced Stock-outs

• Reduced Overstock

• Better Demand Planning

• Improved Inventory Optimization

• Data-driven Decision Making
"""
    )

# ============================================================
# ABOUT PAGE
# ============================================================

elif page == "ℹ️ About":

    st.title("ℹ️ About Project")

    st.markdown("""
## AI-Driven Retail Intelligence & Smart Inventory Optimization Platform

This project predicts retail product demand using Machine Learning
and recommends inventory actions to minimize stock shortages and
overstock situations.

### Machine Learning Models

- Random Forest
- XGBoost
- CatBoost
- LSTM

### Technologies

- Python
- Pandas
- Scikit-Learn
- CatBoost
- Streamlit
- Plotly

### Dataset

73,100 retail transaction records

### Best Model

CatBoost Regression

R² = **0.716**

### Developed By

The Hallunicators team
""")
