import streamlit as st
import pandas as pd
import time
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import japanize_matplotlib
import random

st.title('streamlit Tutorial')

input_num = st.number_input("input_a_number",value=0)
result =input_num ** 2
st.write("Result",result)

df_1 = pd.DataFrame(
    {
        "name":["roadmap","Extras","Issues"],
        "url" :["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars":[random.randint(0,1000) for _ in range(3)],
        "views_history":[[random.randint(0,1000) for _ in range(30)] for _ in range(3)],
    }
)

st.dataframe(
    df_1,
    column_config={
        "name":"App_name",
        "stars": st.column_config.NumberColumn(
            "Github_stars",
            help="number of stars on github",
            format="%d ☆",
        ),
        "url":st.column_config.LinkColumn("app_url"),
        "view_history":st.column_config.LineChartColumn(
            "view(past 30 year)",y_min=0,y_max=5000
        ),
    },
    hide_index=True,
)


df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
})

# DataFrameを表示
st.dataframe(df,hide_index=True)

if st.button('Say hello'):
    st.write('Hello World!')

if st.checkbox('Show/Hide'):
    st.write('Some text')

if st.button("start"):
    with st.spinner("processing...."):
        time.sleep(5)
        st.write("end!!")

st.set_option("deprecation.showPyplotGlobalUse",False)

iris = load_iris()
x,y =iris.data,iris.target

model= DecisionTreeClassifier()
model.fit(x,y)

def plot_model():
    plot_tree(model)
    st.pyplot()
if st.button("plot_model"):
    plot_model()

xx = [i for i in range(100)]
yy = [i*2 for i in range(100)]

str_x = xx[40]
str_y = yy[40] + 10

dfdf = pd.DataFrame()
dfdf["年数"]=xx
dfdf["金額"]=yy
dfdf["備考"]=""

fig = plt.stackplot(xx,yy)
plt.xlabel("年数")
plt.ylabel("金額")
plt.title("収支")
plt.vlines(40 ,0,200, linestyle="dashed" , colors="r")
plt.text(str_x,str_y,"現在",ha="center")
#ax.axvline(40,ls="--",color="r")
st.pyplot()
st.write(dfdf)

