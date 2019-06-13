import numpy as np
import math


class ApplicantPool:

    def __init__(self, pool_size, look_portion=37):
        """
        Constructor for the ApplicantPool class.
        :param pool_size: The total number of applicants in the pool.
        :param look_portion: The percentage size for the look phase. This defaults to 37.
        """
        self.applicant_pool_size = pool_size
        self.how_long_to_look = look_portion
        self.highest_rank = 1
        self.lowest_rank = pool_size
        self.look_list_applicants = None
        self.leap_list_applicants = None
        self.best_applicant_index_whilst_looking = None
        self.best_applicant_rank_whilst_looking = None
        self.top_applicant_index = None
        self.look_list_has_top_applicant = None
        self.leap_list_has_top_applicant = None
        self.chosen_applicant_index = None
        self.chosen_applicant_rank = None
        self.number_of_look_applicants = None
        self.number_of_leap_applicants = None
        self.last_candidate_chosen = None

        # Create an integer array and shuffle the contents.
        # The value of each array element represents the relative ranking of each applicant.
        self.app_pool = np.array(range(pool_size)) + 1
        np.random.shuffle(self.app_pool)

        # Store the number of applicants in the look and leap lists.
        self.look_and_leap_list_sizes()

        # Create lists of look and leap applicants.
        self.look_list_applicants = self.create_look_list()
        self.leap_list_applicants = self.create_leap_list()

        # Find the best applicant in the look list & store their position and rank.
        self.best_applicant_index_whilst_looking = np.argmin(self.look_list_applicants)
        self.best_applicant_rank_whilst_looking = self.look_list_applicants[self.best_applicant_index_whilst_looking]

        # Find the best possible applicant and store their position (their rank will always be 1).
        self.top_applicant_processing()

        # Store the position and rank of the chosen candidate.
        self.chosen_applicant_processing()

    def look_and_leap_list_sizes(self):
        """
        Determine and store the number of applicants in both the look and leap lists.
        """
        self.number_of_look_applicants = math.ceil(self.how_long_to_look * self.applicant_pool_size / 100)
        self.number_of_leap_applicants = self.applicant_pool_size - self.number_of_look_applicants


    def create_look_list(self):
        """
        Creates a list of applicants for the look list.
        :return: A copy of the look list applicants.
        """
        look_pool = self.app_pool[0:self.number_of_look_applicants]

        return look_pool

    def create_leap_list(self):
        """
        Creates a list of applicants for the leap list.
        :return: A copy of the leap phase applicants.
        """
        leap_phase = self.app_pool[self.look_list_applicants.size:]
        return leap_phase

    def top_applicant_processing(self):
        """
        Sets flags that inform whether the top possible candidate exists in the look or the leap list.
        :return: Nothing
        """

        # Does the best possible applicant exist in the look or leap list?
        # There should always be just one single top applicant, find their position.
        top_applicant = np.where(self.app_pool == self.highest_rank)
        self.top_applicant_index = top_applicant[0]

        # Indicate which list the top applicant is in.
        self.look_list_has_top_applicant = (self.top_applicant_index <= self.number_of_look_applicants)
        self.leap_list_has_top_applicant = not self.look_list_has_top_applicant

    def chosen_applicant_processing(self):
        """
        Chooses an applicant based on the selection constraints. See class notes.
        :return: Nothing.
        """
        chosen_applicant = np.where(self.leap_list_applicants < self.best_applicant_rank_whilst_looking)

        if chosen_applicant[0].size == 0:
            # If we can't find a better applicant in the leap list then the job will
            # automatically go to the last candidate. No matter how good they are.
            self.chosen_applicant_index = self.applicant_pool_size - 1
            self.chosen_applicant_rank = self.app_pool[-1]
            self.last_candidate_chosen = True
        else:
            self.chosen_applicant_index = self.number_of_look_applicants + chosen_applicant[0][0]
            self.chosen_applicant_rank = self.app_pool[self.chosen_applicant_index]


