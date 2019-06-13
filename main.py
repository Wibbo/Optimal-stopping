from ApplicantPool import ApplicantPool

# Create a new applicant pool.
# app_pool = ApplicantPool(20)

number_of_cycles = 200
number_of_applicants = 24
top_applicants_chosen = 0




interview_runs = [ApplicantPool(number_of_applicants) for count in range(number_of_cycles)]




for i in interview_runs:
    if i.top_applicant_chosen:
        top_applicants_chosen += 1

top_chosen_percent = top_applicants_chosen / number_of_cycles * 100

print('')
print('')
print('LET''S START HIRING')
print(f'Total number of hiring campaigns: {number_of_cycles}')
print(f'Number of applicants in each campaign: {number_of_applicants}')
print(f'The top applicant was chosen {top_applicants_chosen} times. This gives a {top_chosen_percent}% success rate.')




