import numpy as np
import math


class Campaign:

    def __init__(self, applicant_count, count, can_hire_last_applicant):
        """
        Constructor for the campaigns class.
        This function runs through a number of recruitment campaigns
        to generate outcomes using optimal stopping.
        :param applicant_count: The number of applicants in each campaign.
        :param count: A unique identifier for each campaign.
        """
        global i

        self.can_hire_last_applicant = can_hire_last_applicant
        self.count = count
        self.camp_id = count
        self.applicant_count = applicant_count
        self.applicant_pool = np.arange(applicant_count)
        self.look_for = 37
        self.look_length = math.ceil(applicant_count * self.look_for / 100)
        self.leap_length = applicant_count - self.look_length
        self.offer_made = False

        self.lowest_look_value = applicant_count
        self.lowest_look_index = applicant_count

        self.lowest_leap_value = applicant_count
        self.lowest_leap_index = applicant_count

        self.offered_to_value = applicant_count
        self.offered_to_index = applicant_count

        self.best_chosen = 0
        self.offered_to_last = False
        self.best_is_in_look_list = False
        self.best_is_in_leap_list = False

        np.random.shuffle(self.applicant_pool)

        # Process each applicant in the look phase.
        for i in range(self.look_length):
            if self.applicant_pool[i] < self.lowest_look_value:
                self.lowest_look_value = self.applicant_pool[i]
                self.lowest_look_index = i
            if self.applicant_pool[i] == 0:
                self.best_is_in_look_list = True
                self.best_is_in_leap_list = False

        # Process each applicant in the leap phase.
        for i in range(self.look_length, self.look_length + self.leap_length):
            if self.applicant_pool[i] < self.lowest_leap_value:
                self.lowest_leap_value = self.applicant_pool[i]
                self.lowest_leap_index = i
            if self.applicant_pool[i] == 0:
                self.best_is_in_leap_list = True
                self.best_is_in_look_list = False

            if self.lowest_leap_value < self.lowest_look_value:
                self.offered_to_value = self.lowest_leap_value
                self.offered_to_index = self.lowest_leap_index
                self.offer_made = True
                break
        else:
            # Getting here means the job was offered to the last applicant.
            if self.can_hire_last_applicant:
                self.lowest_leap_index = i
                self.lowest_leap_value = self.applicant_pool[-1]
                self.offered_to_index = i
                self.offered_to_value = self.lowest_leap_value
                self.offered_to_last = True
                self.offer_made = True
            else:
                self.offered_to_index = -1
                self.offered_to_value = -1
                self.offered_to_last = False
                self.offer_made = False

        if self.offered_to_value == 0:
            self.best_chosen = 1
        else:
            self.best_chosen = 0

    def to_dict(self):
        """
        Creates a dictionary from the class which, in turn, provides an easy
        way to create a pandas dataframe from a list of classes.
        :return: A dictionary of class attributes.
        """
        return {
            'id': self.camp_id,
            'applicant_count': self.applicant_count,
            'look_for': self.look_for,
            'look_length': self.look_length,
            'leap_length': self.leap_length,
            'offered_to_last': self.offered_to_last,
            'offered_to_value': self.offered_to_value,
            'offered_to_index': self.offered_to_index,
            'best_chosen': self.best_chosen,
        }

    def __str__(self):
        """
        Override the string description for this class.
        :return: A string describing the class.
        """
        return "Recruitment campaign"


