import streamlit as st
import pandas as pd
import time
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from matplotlib.pyplot as plt

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

fig = plt.plot(xx,yy)
st.pyplot()

