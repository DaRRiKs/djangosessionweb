from django.db import models

class Faculty(models.Model):
    FacultyID = models.AutoField(primary_key=True)
    FacultyName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    def __str__(self):
        return self.FacultyName

class Students(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=150)
    LName = models.CharField(max_length=150)
    Address = models.TextField()
    Email = models.EmailField(max_length=100)
    DateOfBirthDay = models.DateField()
    FacultyID = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.FName} {self.LName}"

class Courses(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    CourseCode = models.CharField(max_length=150)
    Credits = models.IntegerField()
    Description = models.TextField()
    def __str__(self):
        return self.CourseName

class Grades(models.Model):
    GradeID = models.AutoField(primary_key=True)
    GradeLetter = models.CharField(max_length=1)
    GradeNumeric = models.IntegerField()
    def __str__(self):
        return self.GradeLetter

class RecordingToCourse(models.Model):
    RecordID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    GradeID = models.ForeignKey(Grades, on_delete=models.CASCADE)
    RecordingDate = models.DateField()
    Semester = models.CharField(max_length=150)
    AcademicYear = models.CharField(max_length=100)
    def __str__(self):
        return f"Record {self.RecordID}"