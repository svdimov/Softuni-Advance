from project.utest1.project.senior_student import SeniorStudent
from unittest import TestCase,main

class SeniorStudentTest(TestCase):

    def setUp(self):

        self.s = SeniorStudent("1234", "Test", 3.5)

    def test_init(self):
        self.assertEqual('1234',self.s.student_id)
        self.assertEqual('Test',self.s.name)
        self.assertEqual(3.5,self.s.student_gpa)
        self.assertEqual(set(),self.s.colleges)
        s2 = SeniorStudent("5678", "Test2", 3.5)
        self.assertEqual('5678',s2.student_id)
        self.assertEqual('Test2',s2.name)
        self.assertEqual(3.5,s2.student_gpa)
        self.assertEqual(set(), s2.colleges)
        s3 = SeniorStudent("9999", "Test3", 3.8)
        self.assertEqual('9999', s3.student_id)
        self.assertEqual('Test3', s3.name)
        self.assertEqual(3.8, s3.student_gpa)
        self.assertEqual(set(), s3.colleges)



    def test_student_id_validation(self):

        with self.assertRaises(ValueError) as ex:
            self.s.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!",str(ex.exception))

    def test_name_validation(self):

        with self.assertRaises(ValueError) as ex:
            self.s.name = "  "
        self.assertEqual("Student name cannot be null or empty!",str(ex.exception))


    def test_gpa_validation(self):

        with self.assertRaises(ValueError) as ex:
            self.s.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!",str(ex.exception))

    def test_apply_to_college_success(self):

        result = self.s.apply_to_college(3.0, "school")
        self.assertIn("successfully applied", result)
        self.assertIn("SCHOOL", self.s.colleges)

    def test_apply_to_college_failure(self):
        result = self.s.apply_to_college(4.0, "school")
        self.assertEqual(result, "Application failed!")
        self.assertNotIn("SCHOOL", self.s.colleges)


    def test_update_gpa_success(self):

        result = self.s.update_gpa(3.8)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.s.student_gpa, 3.8)

    def test_update_gpa_failure(self):

        result = self.s.update_gpa(0.9)
        self.assertEqual(result, "The GPA has not been changed!")
        self.assertEqual(self.s.student_gpa, 3.5)

    def test_equality_of_students(self):

        s2 = SeniorStudent("5678", "Test2", 3.5)
        self.assertTrue(self.s == s2)

        s3 = SeniorStudent("9999", "Test3", 3.8)
        self.assertFalse(self.s == s3)


if __name__ == '__main__':
    main()

