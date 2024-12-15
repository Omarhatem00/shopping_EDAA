
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


data=pd.read_csv('shopping_cart.csv')
data.drop('Unnamed: 0' , axis=1 , inplace=True)
data['order_date'] = pd.to_datetime(data['order_date'])
data['delivery_date'] = pd.to_datetime(data['delivery_date'])

data['order_year'] = data['order_date'].dt.year
data['order_month'] = data['order_date'].dt.month
data['order_day'] = data['order_date'].dt.day
data['order_weekday'] = data['order_date'].dt.weekday
data["name_day_order"] = data["order_date"].dt.day_name()

data['delivery_year'] = data['delivery_date'].dt.year
data['delivery_month'] = data['delivery_date'].dt.month
data['delivery_day'] = data['delivery_date'].dt.day
data['delivery_weekday'] = data['delivery_date'].dt.weekday
data["name_day_delivery"] = data["delivery_date"].dt.day_name()

data['revenue'] = data['price'] - data['price_per_unit']
data['gross_profit'] = data['revenue'] *data[ 'quantity_x']

color = px.colors.qualitative.Vivid
# what is the total money that each gender spent?
money_gender =data.groupby('gender')[['total_price']].sum().sort_values(by="total_price" , ascending = False).reset_index()
fig1 = px.bar(money_gender,
              x='gender', 
              y= 'total_price' ,
              color_discrete_sequence=color)



# what is the most day that get highest income?
high_day = data.groupby('name_day_order')[['total_price']].sum().sort_values(by='total_price'  , ascending = False).reset_index()
fig2 = px.bar(high_day, x='name_day_order', y= 'total_price' , color_discrete_sequence=color)



# what is the highest month that get the highest sales ?
high_month = data.groupby('order_month')[['total_price']].sum().sort_values(by='total_price' , ascending = False).reset_index()
fig3 = px.bar(high_month, x='order_month', y= 'total_price' , color_discrete_sequence=color)



# what is the highest state achieve the highest salees ?
high_state = data.groupby('state')[['total_price']].sum().sort_values(by='total_price' , ascending = False).reset_index()
fig4= px.bar(high_state, x='state', y='total_price' , color_discrete_sequence=color)



# what is the product type that have the highest sales ?
h_sales=data.groupby(['product_type'])[['total_price']].sum().sort_values(by='total_price' , ascending = False).reset_index()
fig5 = px.pie(h_sales, values='total_price', names='product_type', hole=.3,color_discrete_sequence=color)


#top ages having highest sales.
top_ages=data.groupby(['age'])[['total_price']].sum().sort_values(by='total_price' , ascending = False).reset_index().head(10)
fig6 = px.bar(top_ages, x="age",y= 'total_price' ,color_discrete_sequence=color)




#Which customers are the most loyal ?
loyalty = data.groupby(['customer_name'])[['total_price']].sum().sort_values(by='total_price' , ascending = False).head(10)
fig7 = px.bar(loyalty, y='total_price' , color_discrete_sequence=color)

#profit over year
gross_profit =data.groupby(['order_month'])[['gross_profit']].sum().sort_values(by='order_month' , ascending=False).reset_index()
fig8 = px.line(gross_profit, x="order_month",y= 'gross_profit' , color_discrete_sequence=color)


#revenue over months
revenue_by_date = data.groupby('order_month')[['revenue']].sum().sort_values(by='order_month' , ascending= False).reset_index()
fig9 = px.line(revenue_by_date, x="order_month", y='revenue' , color_discrete_sequence=color)



customer_Purchase_Frequency= data.groupby(['customer_id'])[['order_id']].sum().sort_values(by='customer_id' , ascending=False).reset_index()
fig10 = px.bar(customer_Purchase_Frequency, x='customer_id' , y='order_id' ,color_discrete_sequence=color ,
                   title='Customer Purchase Frequency Distribution') 




# Streamlit Layout
st.title('Shopping_cart_EDA')

# Display the sample data
st.header('Sample Data')
st.dataframe(data, hide_index=True)


# Display visualizations
st.header("How much total money that each gender spent?")
st.plotly_chart(fig1)


st.header("what is the most day that get highest income?")
st.plotly_chart(fig2)


st.header("what is the highest month that get the highest sales ?")
st.plotly_chart(fig3)


st.header("what is the highest state achieve the highest salees ?")
st.plotly_chart(fig4)


st.header("what is the product type that have the highest sales ?")
st.plotly_chart(fig5)


st.header("Top ages having highest sales.")
st.plotly_chart(fig6)


st.header("Which customers are the most loyal ?")
st.plotly_chart(fig7)

st.header("profit over year")
st.plotly_chart(fig8)

st.header("revenue over months")
st.plotly_chart(fig9)

st.header("customer_Purchase_Frequency")
st.plotly_chart(fig10)
