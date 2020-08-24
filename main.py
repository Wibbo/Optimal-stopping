import streamlit as st
from Campaign import Campaign
import pandas as pd
import altair as alt

# Setup the output screen.
st.write('# Recruitment with optimal stopping')
page = st.sidebar.selectbox("Choose a page", ['Introduction', 'Simulation', 'About'])

number_of_cycles = 300
number_of_applicants = 100

if page == 'Introduction':
    st.write('Explanation goes here')

if page == 'Simulation':
    st.sidebar.markdown('')
    st.sidebar.markdown('## Application parameters')
    number_of_cycles = st.sidebar.slider('Number of campaigns', 100, 5000, 300, 100)
    number_of_applicants = st.sidebar.slider('Number of applicants', 100, 5000, 100, 100)

top_applicant_chosen = 0
top_applicant_in_look_list = 0
top_applicant_in_leap_list = 0
top_applicant_last = 0

campaigns = [Campaign(number_of_applicants, count) for count in range(number_of_cycles)]
df = pd.DataFrame.from_records([s.to_dict() for s in campaigns])

df['best_app'] = df['best_chosen'].expanding().sum()

for i in campaigns:
    if i.offered_to_value == 0:
        top_applicant_chosen += 1
    if i.best_is_in_look_list:
        top_applicant_in_look_list += 1


top_chosen_percent = round(top_applicant_chosen / number_of_cycles * 100, 1)

if page == 'Simulation':
    st.write('')
    st.write('## CAMPAIGN RESULTS')
    st.write(f'Number of recruitment campaigns: {number_of_cycles}')
    st.write(f'Number of applicants in each campaign: {number_of_applicants}')
    st.write(f'** The best applicant was chosen {top_chosen_percent}% of the time. **')
    st.write('')
    st.write('')

    line = alt.Chart(df).mark_line().encode(
        x='id',
        y='best_app'
    )
    line.title = 'Times the best candidate was chosen'
    line.encoding.x.title = 'Current campaign'
    line.encoding.y.title = 'Sum of best candidate chosen'
    line
