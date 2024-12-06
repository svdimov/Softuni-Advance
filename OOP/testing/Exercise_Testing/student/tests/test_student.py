from project import Student
from unittest import TestCase, main


class StudentTest(TestCase):
    def setUp(self):
        self.student_1 = Student("Student1",
                                 {"Python": ["n1", "n2", "n3"],
                                  "JS": ["n1", "n1"]})

        self.student_2 = Student("Student2")

    def test_init_with_courses(self):
        self.assertEqual('Student1', self.student_1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"],
                          "JS": ["n1", "n1"]}, self.student_1.courses)
        self.assertIsInstance(self.student_1.name, str)
        self.assertIsInstance(self.student_1.courses, dict)

    def test_init_with_none_courses(self):
        self.assertEqual("Student2", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

        self.assertIsInstance(self.student_2.name, str)
        self.assertIsInstance(self.student_2.courses, dict)

    def test_enroll_existing_course(self):

        result = self.student_1.enroll("Python",["n4","n5"],"Y")
        self.assertEqual("Course already added. Notes have been updated.",result)
        self.assertEqual({"Python": ["n1", "n2", "n3","n4","n5"],
                          "JS": ["n1", "n1"]},self.student_1.courses)

        result = self.student_1.enroll("Python", ["n6", "n7"], "N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5","n6", "n7"],
                          "JS": ["n1", "n1"]}, self.student_1.courses)

    def test_enroll_not_existing_course_add_note_Y(self):
        result = self.student_1.enroll("C#",["n1","n2"],"Y")
        self.assertEqual("Course and course notes have been added.",result)
        self.assertIn("C#",self.student_1.courses)
        self.assertEqual(["n1","n2"],self.student_1.courses["C#"])

    def test_enroll_not_existing_course_add_empty_str(self):
        result = self.student_1.enroll("C#",["n1","n2"],"")
        self.assertEqual("Course and course notes have been added.",result)
        self.assertIn("C#",self.student_1.courses)
        self.assertEqual(["n1","n2"],self.student_1.courses["C#"])

    def test_enroll_not_notes(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertIn("C#", self.student_1.courses)
        self.assertEqual([], self.student_1.courses["C#"])

    def test_add_notes_to_existing_course(self):
        result = self.student_1.add_notes("JS","n3")
        self.assertEqual(result,"Notes have been updated")
        self.assertEqual(["n1", "n1","n3"],self.student_1.courses["JS"])
    def test_add_note_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("C+","n1")
        self.assertEqual(str(ex.exception),"Cannot add notes. Course not found.")
    def test_leave_courses_existing(self):
        result = self.student_1.leave_course("Python")
        self.assertEqual("Course has been removed",result)
        self.assertNotIn("Python",self.student_1.courses)

    def test_leave_courses_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("C++")
        self.assertEqual(str(ex.exception),"Cannot remove course. Course not found.")


if __name__ == '__main__':
    main()
