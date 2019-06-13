from unittest import TestCase
from ApplicantPool import ApplicantPool


class TestApplicantPool(TestCase):

    def setUp(self):
        self.pool = ApplicantPool(30)

    def test_default_look_ratio(self):
        self.assertEqual(self.pool.how_long_to_look, 37)

    def test_specified_look_ratio(self):
        p1 = ApplicantPool(40, 41)
        self.assertEqual(p1.how_long_to_look, 41)

    def test_applicant_pool_size_1(self):
        p1 = ApplicantPool(40)
        self.assertEqual(p1.applicant_pool_size, 40)

    def test_applicant_pool_size_2(self):
        p1 = ApplicantPool(400)
        self.assertEqual(p1.applicant_pool_size, 400)

    def test_size_of_look_list_1(self):
        p1 = ApplicantPool(200, 50)
        self.assertEqual(p1.number_of_look_applicants, 100)

    def test_size_of_look_list_2(self):
        p1 = ApplicantPool(99, 50)
        self.assertEqual(p1.number_of_look_applicants, 50)

    def test_size_of_leap_list_1(self):
        p1 = ApplicantPool(200, 38)
        self.assertEqual(p1.number_of_leap_applicants, 124)

    def test_size_of_leap_list_2(self):
        p1 = ApplicantPool(99, 50)
        self.assertEqual(p1.number_of_leap_applicants, 49)

    def test_highest_rank_1(self):
        p1 = ApplicantPool(200)
        self.assertEqual(p1.highest_rank, 1)

    def test_highest_rank_2(self):
        p1 = ApplicantPool(173)
        self.assertEqual(p1.highest_rank, 1)

    def test_lowest_rank_1(self):
        p1 = ApplicantPool(200)
        self.assertEqual(p1.lowest_rank, 200)

    def test_lowest_rank_2(self):
        p1 = ApplicantPool(173)
        self.assertEqual(p1.lowest_rank, 173)

    def test_applicant_list_entries_1(self):
        p1 = ApplicantPool(100)
        self.assertEqual(p1.app_pool.size, p1.applicant_pool_size)

    def test_applicant_list_entries_2(self):
        p1 = ApplicantPool(2999)
        self.assertEqual(p1.app_pool.size, p1.applicant_pool_size)

