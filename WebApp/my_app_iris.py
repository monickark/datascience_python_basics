import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# header of web app
st.write("""
# Simple Iris flower prediction

This app predict the iris flower type 
""")

st.sidebar.header("User input parameters")

def user_input_features():
    sepal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)

    data = {
        "Sepal Length" : sepal_length,
        "Sepal Width" : sepal_width,
        "Petal Length" : petal_length,
        "Petal Width" : petal_width
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.header("Input Parameters")
st.write(input_df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

predic = clf.predict(input_df)
predic_prob = clf.predict_proba(input_df)

st.write("Label vs Index")
st.write(iris.target_names)

st.write("Prediction")
st.write(iris.target_names[predic])
#st.write(predic)

st.write("Prediction Probability")
st.write(predic_prob)