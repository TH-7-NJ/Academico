from django.db import models
from datetime import date, timedelta

class Uf(models.Model):
    name = models.CharField(max_length=2, verbose_name="State abbreviation")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State (UF)"
        verbose_name_plural = "States (UFs)"


class City(models.Model):
    name = models.CharField(max_length=99, verbose_name="City name")
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE, verbose_name="State (UF)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Ocupation(models.Model):
    name = models.CharField(max_length=99, verbose_name="Occupation name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Occupation"
        verbose_name_plural = "Occupations"


class Person(models.Model):
    name = models.CharField(max_length=99, verbose_name="Full name")
    father_name = models.CharField(max_length=99, verbose_name="Father's name")
    mother_name = models.CharField(max_length=99, verbose_name="Mother's name")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    birthday = models.DateField(verbose_name="Birthday", default=date.today)
    email = models.CharField(max_length=99, verbose_name="Email")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City")
    ocupation = models.ForeignKey(Ocupation, on_delete=models.CASCADE, verbose_name="Occupation")

    def __str__(self):
        return f'{self.name}, {self.cpf}'

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"


class EducationalInstitution(models.Model):
    name = models.CharField(max_length=99, verbose_name="Institution name")
    website = models.CharField(max_length=99, verbose_name="Website")
    phone = models.CharField(max_length=13, verbose_name="Phone number")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Educational Institution"
        verbose_name_plural = "Educational Institutions"


class KnowledgeArea(models.Model):
    name = models.CharField(max_length=99, verbose_name="Knowledge area")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Knowledge Area"
        verbose_name_plural = "Knowledge Areas"


class Course(models.Model):
    name = models.CharField(max_length=99, verbose_name="Course name")
    workload = models.FloatField(verbose_name="Workload")
    month_duration = models.IntegerField(verbose_name="Duration in months")
    knowledgeArea = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE, verbose_name="Knowledge area")
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, verbose_name="Institution")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Shift(models.Model):
    name = models.CharField(max_length=99, verbose_name="Shift name")
    morning = models.BooleanField(verbose_name="Morning shift")
    nocturnal = models.BooleanField(verbose_name="Nocturnal shift")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"


class Discipline(models.Model):
    name = models.CharField(max_length=99, verbose_name="Discipline name")
    knowledgeArea = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE, verbose_name="Knowledge area")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"


class Register(models.Model):
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, verbose_name="Institution")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline")
    start_date = models.DateField(verbose_name="Start date", default=date.today)
    end_date_prevision = models.DateField(verbose_name="Estimated end date", default=date.today() + timedelta(days=365*4))

    def __str__(self):
        return f"{self.institution}, {self.course}, {self.discipline}"

    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Registers"


class AvaliationType(models.Model):
    name = models.CharField(max_length=99, verbose_name="Type name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Avaliation Type"
        verbose_name_plural = "Avaliation Types"


class Avaliation(models.Model):
    description = models.CharField(max_length=300, verbose_name="Description")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline")
    grade = models.FloatField(verbose_name="Grade")
    type = models.ForeignKey(AvaliationType, on_delete=models.CASCADE, verbose_name="Avaliation Type")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Avaliation"
        verbose_name_plural = "Avaliations"


class Frequence(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person")
    fault_number = models.IntegerField(verbose_name="Number of faults")

    def __str__(self):
        return f"{self.person} - {self.discipline}"

    class Meta:
        verbose_name = "Frequence"
        verbose_name_plural = "Frequences"


class Session(models.Model):
    name = models.CharField(max_length=99, verbose_name="Session name")
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, verbose_name="Shift")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"


class Ocorrence(models.Model):
    description = models.CharField(max_length=300, verbose_name="Description")
    date = models.DateField(verbose_name="Date", default=date.today)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Occurrence"
        verbose_name_plural = "Occurrences"


class DisciplinesPerCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline")
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, verbose_name="Shift")
    workload = models.FloatField(verbose_name="Workload")

    def __str__(self):
        return f"{self.discipline} - {self.course}"

    class Meta:
        verbose_name = "Discipline per Course"
        verbose_name_plural = "Disciplines per Course"


class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Student")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline")
    avaliation = models.ForeignKey(Avaliation, on_delete=models.CASCADE, verbose_name="Avaliation")
    frequence = models.ForeignKey(Frequence, on_delete=models.CASCADE, verbose_name="Frequence")

    def __str__(self):
        return f"{self.person} - {self.discipline}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
