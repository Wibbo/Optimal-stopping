import streamlit as st
from Campaign import Campaign
import pandas as pd
import numpy as np

# Setup the output screen.
st.write('# Recruitment with optimal stopping')
st.sidebar.markdown('')
st.sidebar.markdown('## Application parameters')

number_of_cycles = st.sidebar.slider('Number of campaigns', 100, 5000, 300, 100)
number_of_applicants = st.sidebar.slider('Number of applicants', 100, 5000, 300, 100)
show_details = st.sidebar.checkbox('Show details (first 10 campaigns)', True)

top_applicant_chosen = 0
top_applicant_in_look_list = 0
top_applicant_in_leap_list = 0
top_applicant_last = 0

campaigns = [Campaign(number_of_applicants) for count in range(number_of_cycles)]
df = pd.DataFrame.from_records([s.to_dict() for s in campaigns])

for i in campaigns:
    if i.offered_to_value == 0:
        top_applicant_chosen += 1
    if i.best_is_in_look_list:
        top_applicant_in_look_list += 1

if show_details:
    for j in range(10):
        st.write(f'#### Campaign number {j}')
        st.write(f'Best ranked candidate in look phase: {campaigns[j].lowest_look_value}')
        st.write(f'Best ranked candidate in leap phase: {campaigns[j].lowest_leap_value}')
        st.write(f'Last candidate was offered the job?: {campaigns[j].offered_to_last}')

top_chosen_percent = round(top_applicant_chosen / number_of_cycles * 100, 1)

st.write('')
st.write('## CAMPAIGN RESULTS')
st.write(f'Number of recruitment campaigns: {number_of_cycles}')
st.write(f'Number of applicants in each campaign: {number_of_applicants}')
st.write(f'** The best applicant was chosen {top_applicant_chosen} times. This gives a {top_chosen_percent}% success rate. **')

st.line_chart(df['offered_to_index'])

st.line_chart(df['offered_to_value'])



