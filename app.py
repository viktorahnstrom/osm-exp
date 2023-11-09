import streamlit as st
import random
#import pandas as pd
#import seaborn as sns

#st.title("open science methods, python")
#st.title("ab test, online survey experiment")
#st.header()
#st.subheader("open science methods, python")
#st.text()
st.markdown("open science methods, python")

conditions = ["a", "b"]
selected_condition = random.choice(conditions)

if selected_condition == "a":
    st.image("img/exps-stim-c.png")
else:
    st.image("img/exps-stim-t.png")

#form = st.form("some_form")
#option = form.radio(
#    "please look at the advert and rate your attitude towards the product",
#    ["1", "2", "3", "4", "5"],
#    captions = ["strongly negative", "negative", "neither", "positive", "strongly positive"], horizontal=True)

#if rating == '3':
#    st.write('selected neither')
#else:
#    st.write("negative or positive")

with st.form("my_form"):
#   st.write("Inside the form")
#   slider_val = st.slider("Form slider")
#   checkbox_val = st.checkbox("Form checkbox")
    option_val = st.radio("please look at the advert and rate your attitude towards the product", ["1", "2", "3", "4", "5"], captions = ["strongly negative", "negative", "neither", "positive", "strongly positive"], horizontal=True)

    # form must have a submit button.
    submitted = st.form_submit_button("submit")
    if submitted:
        st.write("option", option_val)

st.write("check out this link: [osm-py](%s)" % "https://nils-holmberg.github.io/socs-qmd/web/osm-py/about.html")








