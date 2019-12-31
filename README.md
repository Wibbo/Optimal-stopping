# HELLO SIMON
# Simulating recruitment campaigns using an optimal stopping strategy

## A little about the theory
Based on the rules below, optimal stopping provides a strategy for hiring the top applicant in a given applicant pool. The approach that this simulation tests, should find the best applicant, on average, 37% of the time. 

![Process flow diagram](https://github.com/Wibbo/Optimal-stopping/blob/master/images/Optimal_Stopping_Flow_01.jpg)

## Rules of the simulation
This simulator uses a 'look before leaping' algorithm to try and optimise the process of hiring a great data 
scientist. There are a number of constraints that apply, the algorithm will:

- Allow a configurable number of data scientists to be specified for each interview campaign.
- Allow the number of campaigns that are simulated to be specified.
- Only rank each applicant with respect to the other candidates that have already been interviewed. 
- Assign each applicant a number that defines how they are rated in relation to each other. 
- Randomly order the applicants in each recruitment campaign.
- Have no other information about each applicant. It can only relate each of the interviewees to each other.
- Must hire an applicant immediately after their interview finishes or accept that they are gone forever. 

## Files in the repository
- main.py 
Runs a number of recruitment campaigns and prints summary results to the Console window.
- secretary.ipynb
A Jupyter notebook file providing additional configuration and output information.
- ApplicantPool.py
A class that represents a pool of applicants.
- Campaigns.py
A class providing summary information for a recruitment campaign.
- test_applicantPool.py
A group of associated unit tests.



