from project.student import Student
from unittest import TestCase,main

import unittest

class TestStudent(unittest.TestCase):
    def setUp(self):
        """Set up a test case for the Student class."""
        self.student = Student("John")

    def test_init(self):
        """Test the __init__ method of the Student class."""
        student = Student("Alice")
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.courses, {})

        student_with_courses = Student("Bob", {"Math": ["Note1"]})
        self.assertEqual(student_with_courses.name, "Bob")
        self.assertEqual(student_with_courses.courses, {"Math": ["Note1"]})

    def test_enroll_existing_course(self):
        """Test enrolling in an existing course updates the notes."""
        self.student.courses = {"Math": ["Note1"]}
        result = self.student.enroll("Math", ["Note2"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["Math"], ["Note1", "Note2"])

    def test_enroll_new_course_with_notes(self):
        """Test enrolling in a new course with notes."""
        result = self.student.enroll("Science", ["Note1"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["Science"], ["Note1"])

    def test_enroll_new_course_without_notes(self):
        """Test enrolling in a new course without adding notes explicitly."""
        result = self.student.enroll("History", ["Note1"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["History"], ["Note1"])

    def test_enroll_new_course_decline_notes(self):
        """Test enrolling in a new course but declining to add notes."""
        result = self.student.enroll("Art", ["Note1"], "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses["Art"], [])

    def test_add_notes_existing_course(self):
        """Test adding notes to an existing course."""
        self.student.courses = {"Math": ["Note1"]}
        result = self.student.add_notes("Math", "Note2")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["Math"], ["Note1", "Note2"])

    def test_add_notes_nonexistent_course(self):
        """Test adding notes to a non-existent course raises an exception."""
        with self.assertRaises(Exception) as context:
            self.student.add_notes("Physics", "Note1")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_course_existing(self):
        """Test leaving an existing course."""
        self.student.courses = {"Math": ["Note1"], "History": ["Note1"]}
        result = self.student.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertNotIn("Math", self.student.courses)

    def test_leave_course_nonexistent(self):
        """Test leaving a non-existent course raises an exception."""
        with self.assertRaises(Exception) as context:
            self.student.leave_course("Biology")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")

if __name__ == "__main__":
    unittest.main()
