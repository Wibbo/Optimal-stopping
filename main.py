import streamlit as st
from Campaign import Campaign
import pandas as pd
import plotly_express as px


# Setup the output screen.
st.write('# Recruitment with optimal stopping')


st.sidebar.markdown('')
st.sidebar.image('./images/Obj1.png', width=300)
st.sidebar.markdown('## Application parameters')
number_of_cycles = st.sidebar.slider('Number of campaigns', 100, 500, 300, 10)
number_of_applicants = st.sidebar.slider('Number of applicants', 100, 500, 100, 10)
show_details = st.sidebar.checkbox('Show details')
hire_last = st.sidebar.checkbox('Hire last applicant?')
st.write('')
st.sidebar.markdown('## MORE INFORMATION')
st.sidebar.markdown("<a href='https://bit.ly/3jVfHpz'>What is optimal stopping</a>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='https://bit.ly/2RhTohL'>The code is on GitHub</a>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='https://www.objectivity.co.uk'>Objectivity web site</a>", unsafe_allow_html=True)
st.sidebar.markdown("Email mweaver@objectivity.co.uk")

top_applicant_chosen = 0
top_applicant_in_look_list = 0
top_applicant_in_leap_list = 0
top_applicant_last = 0
offered_to_last = 0
offers_made = 0

# Create and process each campaign.
campaigns = [Campaign(number_of_applicants, count, hire_last) for count in range(number_of_cycles)]
df = pd.DataFrame.from_records([s.to_dict() for s in campaigns])
average_interviews = df['offered_to_index'].mean()

candidate_data = pd.DataFrame(columns=('campaign', 'index', 'best chosen', 'value', 'offered'))

# Determine summary data.
for i in campaigns:
    if i.offered_to_value == 0:
        top_applicant_chosen += 1
    if i.best_is_in_look_list:
        top_applicant_in_look_list += 1
    if i.offered_to_last:
        offered_to_last += 1
    if i.offer_made:
        offers_made += 1
    if show_details:
        candidate_data.loc[i] = [i.camp_id, i.offered_to_index, i.best_chosen, i.offered_to_value, i.offer_made]

candidate_data.set_index('campaign')

last_chosen_percent = round(offered_to_last / number_of_cycles * 100, 1)
top_chosen_percent = round(top_applicant_chosen / number_of_cycles * 100, 1)
people_in_look = round(df['look_length'][0], 0)

st.write('')
st.write('## CAMPAIGN RESULTS')
st.write(f'In total {offers_made} job offers were made across {number_of_cycles} campaigns.')
st.write(f'Number of applicants in each campaign: {number_of_applicants}')
st.write(f'Number of applicants in the look phase: {people_in_look}')
st.write(f'** The last applicant was offered a job {last_chosen_percent}% of the time. **')
st.write(f'** The best applicant was offered a job {top_chosen_percent}% of the time. **')
st.write('')

offered_positions = df[df.offered_to_index > 0]
offered_ranking = df[df.offered_to_value > -1]

fig = px.histogram(offered_positions, x='offered_to_index', nbins=10,
                   labels={
                       'offered_to_index': 'Interview position',
                   },
                   title='Job offers made by interview position'
                   )

st.plotly_chart(fig)

fig = px.histogram(offered_positions, x='offered_to_value', nbins=10,
                   labels={
                       'offered_to_value': 'Relative ranking',
                   },
                   title='Job offers made by relative ranking'
                   )

st.plotly_chart(fig)

if show_details:
    summary_text = 'Index is the order in which each applicant is interviewed, starting at zero. '
    summary_text += 'So an index of 32 means this is the 33rd applicant that was interviewed. '
    summary_text += 'Value is the relative ranking of each applicant, zero being the best.'
    st.write('## RECORD OF JOB OFFERS')
    st.dataframe(candidate_data.style.highlight_max(axis=0))
    st.write(summary_text)


