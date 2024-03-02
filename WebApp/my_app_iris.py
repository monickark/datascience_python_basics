import streamlit as st
import pandas as pd
from sklearn import dataset
from sklearn ensemble import RandomForestClassifier

# header of web app
st.write("""
# Simple Iris flower prediction

This app predict the iris flower type 
""")

st.sidebar.header("User input parameters")

def user_input_features():
    sepal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("Sepal Width", 4.3, 7.9, 5.4)
    petal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    petal_width = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)

    data = {
        "Sepal Length" : sepal_length,
        "Sepal Width" : sepal_width,
        "Petal Length" : petal_length,
        "Petal Width" : petal_width
    }

    features = pd.Dataframe(data, index[0])
    return features

input_df = user_input_features()

st.header("Input Parameters")
st.write(input_df)

iris = dataset.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

predic = clf.predict()
predic_prob = clf.predict_proba()

st.write("Label vs Index")
st.write(iris.target_names)

st.write("Prediction")
st.write(predic)

st.write("Prediction Probability")
st.write(predic_prob)