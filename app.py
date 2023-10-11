import streamlit as st
import random
#import pandas as pd
#import seaborn as sns

st.title("open science methods, python")

st.title("ab test, online survey experiment")

conditions = ["a", "b"]
selected_condition = random.choice(conditions)

if selected_condition == "a":
    st.image("img/exps-stim-c.png")
else:
    st.image("img/exps-stim-t.png")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."], horizontal=True)

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")


st.write("check out this link: [osm-py](%s)" % "https://nils-holmberg.github.io/socs-qmd/web/osm-py/about.html")








