import streamlit as st
from Campaign import Campaign
import pandas as pd
import altair as alt

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
st.sidebar.markdown("<a href='https://medium.com/@matt_r_weaver/recruiting-in-a-rush-read-on-70a19087e3b6'>What is optimal stopping</a>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='https://github.com/Wibbo/Optimal-stopping'>The code is on GitHub</a>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='https://www.streamlit.io/'>Read more about Streamlit here</a>", unsafe_allow_html=True)
st.sidebar.markdown("Email mweaver@objectivity.co.uk")




top_applicant_chosen = 0
top_applicant_in_look_list = 0
top_applicant_in_leap_list = 0
top_applicant_last = 0
offered_to_last = 0
offers_made = 0

campaigns = [Campaign(number_of_applicants, count, hire_last) for count in range(number_of_cycles)]
df = pd.DataFrame.from_records([s.to_dict() for s in campaigns])

df['best_app'] = df['best_chosen'].expanding().sum()
candidate_data = pd.DataFrame(columns=('campaign', 'index', 'value', 'offered'))

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
        candidate_data.loc[i] = [i.camp_id, i.offered_to_index, i.offered_to_value, i.offer_made]

candidate_data.set_index('campaign')

last_chosen_percent = round(offered_to_last / number_of_cycles * 100, 1)
top_chosen_percent = round(top_applicant_chosen / number_of_cycles * 100, 1)

st.write('')
st.write('## CAMPAIGN RESULTS')
st.write(f'Number of recruitment campaigns: {number_of_cycles}')
st.write(f'Number of applicants in each campaign: {number_of_applicants}')
st.write(f'In total {offers_made} offers were made.')
st.write(f'** The last applicant was chosen {last_chosen_percent}% of the time. **')
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

if show_details:
    st.write('## RECORD OF JOB OFFERS')
    st.dataframe(candidate_data.style.highlight_max(axis=0))
    st.write('Index is the order in which each applicant is interviewed, starting at zero. So an index of 32 means this is the 33rd applicant that was interviewed.')
    st.write('Value is the relative ranking of each applicant, zero being the best.')
