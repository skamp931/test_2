import streamlit as st
import pandas as pd
import time
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import japanize_matplotlib

input_num = st.number_input("input_a_number",value=0)

result =input_num ** 2
st.write("Result",result)

st.title('streamlit Tutorial')

st.header('This is a header')

st.subheader('This is a subheader')

st.text('Hello World!')

st.write('# headline1')

st.markdown('# headline2')

st.write(['apple', 'orange', 'banana'])

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
})

# DataFrameを表示
st.write(df)
# st.dataframe()でも表示可能
st.dataframe(df)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(uploaded_file)

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

