from django.db import models
from django.utils.timezone import now
import django
from datetime import datetime, timedelta

class Occupation(models.Model):
    name = models.CharField(max_length=99, verbose_name="Occupation's name", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Occupation"
        verbose_name_plural = "occupations"

class City(models.Model):
    name = models.CharField(max_length=99, verbose_name="City's name", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

class Uf(models.Model):
    name = models.CharField(max_length=2, verbose_name="UF's name", null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City's name", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "UF"
        verbose_name_plural = "UFs"

class Person(models.Model):
    name = models.CharField(max_length=99, verbose_name="Person's name", null=True, blank=True)
    father_name = models.CharField(max_length=99, verbose_name="Person's father's name", null=True, blank=True)
    mother_name = models.CharField(max_length=99, verbose_name="Person's mother's name", null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="Person's CPF", null=True, blank=True)
    birthday = models.DateField(verbose_name="Person's birthday", default=now)
    email = models.CharField(max_length=99, verbose_name="Person's email", null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Person's city", null=True, blank=True)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, verbose_name="Person's occupation", null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.cpf}'
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

class EducationalInstitution(models.Model):
    name = models.CharField(max_length=99, verbose_name="Institution's name", null=True, blank=True)
    website = models.CharField(max_length=99, verbose_name="Institution's website", null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name="Instituion's phone number", null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Person's city", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Educational Institution"
        verbose_name_plural = "Educational Institutions"

class KnowledgeArea(models.Model):
    name = models.CharField(max_length=99, verbose_name="Area's name", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Knowledge area"
        verbose_name_plural = "Knowledge areas"
        
class Shift(models.Model):
    name = models.CharField(max_length=99, verbose_name="Shift type", null=True, blank=True)
    morning = models.BooleanField(verbose_name="Morning shift", null=True, blank=True)
    nocturnal = models.BooleanField(verbose_name="Nocturnal shift", null=True, blank=True)  
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"

class Discipline(models.Model):
    name = models.CharField(max_length=99, verbose_name="Discipline's name", null=True, blank=True)
    knowledgeArea = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE, verbose_name="Course's area", null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"

class Course(models.Model):
    name = models.CharField(max_length=99, verbose_name="Course's name", null=True, blank=True)
    workload = models.FloatField(verbose_name="Course's workload", null=True, blank=True)
    knowledgeArea = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE, verbose_name="Course's area", null=True, blank=True)
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, verbose_name="Course's institution", null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Course's discipline", null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

class Register(models.Model):
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, verbose_name="Educational institution", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", null=True, blank=True) 
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline", null=True, blank=True)
    start_date = models.DateField(verbose_name="Register's start date", default=now)
    end_date_prevision = models.DateField(verbose_name="Register's end date prevision", default=datetime.now() + timedelta(days=365*4))

    def __str__(self):
        return f"{self.institution}, {self.course}, {self.discipline}" 
    
    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Registers"

class AvaliationType(models.Model):
    name = models.CharField(max_length=99, verbose_name="Avaliation type's name", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Avaliation Type"
        verbose_name_plural = "Avaliations Types"

class Frequence(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", null=True, blank=True) 
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline", null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person", null=True, blank=True)
    fault_number = models.IntegerField(verbose_name="Person's number of faults", null=True, blank=True)

    def __str__(self):
        return f"{self.discipline}, {self.course}"
    
    class Meta:
        verbose_name = "Frequence"
        verbose_name_plural = "Frequences"

class Avaliation(models.Model):
    description = models.CharField(max_length=300, verbose_name="Avaliation's description", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", null=True, blank=True) 
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline", null=True, blank=True)
    grade = models.FloatField(verbose_name="Avaliation's grade")
    type = models.CharField(max_length=99, verbose_name="Avaliation's type", null=True, blank=True)
    student = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Student", limit_choices_to={'occupation':'student'}, null=True, blank=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Avaliation"
        verbose_name_plural = "Avaliations"

class Session(models.Model):
    name = models.CharField(max_length=99, verbose_name="Session's name", null=True, blank=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, verbose_name="Session's shift", null=True, blank=True)
    student = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Student", limit_choices_to={'occupation':'student'}, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"


class Ocorrence(models.Model):
    description = models.CharField(max_length=300, verbose_name="Ocorrence's description", default=now)
    date = models.DateField(verbose_name="Ocorrence's date", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", null=True, blank=True) 
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline", null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person", null=True, blank=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Ocorrence"
        verbose_name_plural = "Ocorrences"

class DisciplinesPerCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", null=True, blank=True) 
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline", null=True, blank=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, verbose_name="Session's shift", null=True, blank=True)
    workload = models.FloatField(verbose_name="Course's workload", null=True, blank=True)

    def __str__(self):
        return f"{self.discipline}, {self.course}"
    
    class Meta:
        verbose_name = "Disciplines per course"
        verbose_name_plural = "Disciplines per courses"

