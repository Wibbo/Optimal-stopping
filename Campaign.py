import numpy as np
import math


class Campaign:

    def __init__(self, applicant_count):

        """
        Constructor for campaigns.
        Basically this handles everything for now/
        :param applicant_count: The number of applicants.
        """
        self.applicant_count = applicant_count
        self.applicant_pool = np.arange(applicant_count)
        self.look_for = 37
        self.look_length = math.ceil(applicant_count * self.look_for / 100)
        self.leap_length = applicant_count - self.look_length

        self.lowest_look_value = applicant_count
        self.lowest_look_index = applicant_count

        self.lowest_leap_value = applicant_count
        self.lowest_leap_index = applicant_count

        self.offered_to_value = applicant_count
        self.offered_to_index = applicant_count

        self.best_chosen = False
        self.offered_to_last = False
        self.best_is_in_look_list = False
        self.best_is_in_leap_list = False

        np.random.shuffle(self.applicant_pool)

        for i in range(self.look_length):
            if self.applicant_pool[i] < self.lowest_look_value:
                self.lowest_look_value = self.applicant_pool[i]
                self.lowest_look_index = i
            if self.applicant_pool[i] == 0:
                self.best_is_in_look_list = True
                self.best_is_in_leap_list = False

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
                break
        else:
            self.lowest_leap_index = i
            self.lowest_leap_value = self.applicant_pool[-1]
            self.offered_to_index = i
            self.offered_to_value = self.lowest_leap_value
            self.offered_to_last = True

    def to_dict(self):
        return {
            'applicant_count': self.applicant_count,
            'look_for': self.look_for,
            'look_length': self.look_length,
            'leap_length': self.leap_length,
            'offered_to_last': self.offered_to_last,
            'offered_to_value': self.offered_to_value,
            'offered_to_index': self.offered_to_index,
        }



