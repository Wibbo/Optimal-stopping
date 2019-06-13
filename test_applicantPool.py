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