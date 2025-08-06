from unittest import TestCase, main
from project.student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Martin")

    def test_initialization(self):
        self.assertEqual(self.student.name, "Martin")
        self.assertEqual(self.student.courses, {})

    def test_initialization_with_courses(self):
        courses = {"Math": ["Algebra", "Calculus"]}
        student = Student("Bratan", courses)
        self.assertEqual(student.name, "Bratan")
        self.assertEqual(student.courses, courses)

    def test_enroll_existing_course_adds_notes(self):
        self.student.courses = {"History": ["Intro"]}
        result = self.student.enroll("History", ["WW2"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["History"], ["Intro", "WW2"])

    def test_enroll_new_course_with_notes_when_Y(self):
        result = self.student.enroll("Biology", ["Cells"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["Biology"], ["Cells"])

    def test_enroll_new_course_with_notes_when_empty_str(self):
        result = self.student.enroll("Physics", ["Motion"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["Physics"], ["Motion"])

    def test_enroll_new_course_without_notes(self):
        result = self.student.enroll("Chemistry", ["Atoms"], "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses["Chemistry"], [])

    def test_add_notes_successfully(self):
        self.student.courses = {"Art": ["Painting"]}
        result = self.student.add_notes("Art", "Sculpture")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["Art"], ["Painting", "Sculpture"])

    def test_add_notes_raises_if_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Programming", "C Language")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")
        self.assertEqual(self.student.courses, {})

    def test_leave_course_successfully(self):
        self.student.courses = {"Geography": ["Maps"]}
        result = self.student.leave_course("Geography")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student.courses, {})

    def test_leave_course_raises_if_not_found(self):
        self.student.courses = {"Geography": ["Maps"]}
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")
        self.assertEqual(self.student.courses, {"Geography": ["Maps"]})


if __name__ == "__main__":
    main()
