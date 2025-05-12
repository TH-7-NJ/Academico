from django.contrib import admin
from .models import (
    Uf, City, Ocupation, Person, EducationalInstitution, KnowledgeArea, Course,
    Shift, Discipline, Register, AvaliationType, Avaliation, Frequence,
    Session, Ocorrence, DisciplinesPerCourse, Student
)

@admin.register(Uf)
class UfAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'uf']
    search_fields = ['name']
    list_filter = ['uf']


@admin.register(Ocupation)
class OcupationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'email', 'city', 'ocupation']
    search_fields = ['name', 'cpf', 'email']
    list_filter = ['city', 'ocupation']


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'phone', 'city']
    search_fields = ['name']
    list_filter = ['city']


@admin.register(KnowledgeArea)
class KnowledgeAreaAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'knowledgeArea', 'month_duration', 'workload']
    search_fields = ['name']
    list_filter = ['institution', 'knowledgeArea']


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'morning', 'nocturnal']
    search_fields = ['name']


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name', 'knowledgeArea']
    search_fields = ['name']
    list_filter = ['knowledgeArea']


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['institution', 'course', 'discipline', 'start_date', 'end_date_prevision']
    list_filter = ['institution', 'course', 'discipline']
    date_hierarchy = 'start_date'


@admin.register(AvaliationType)
class AvaliationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Avaliation)
class AvaliationAdmin(admin.ModelAdmin):
    list_display = ['description', 'course', 'discipline', 'grade', 'type']
    search_fields = ['description']
    list_filter = ['course', 'discipline', 'type']


@admin.register(Frequence)
class FrequenceAdmin(admin.ModelAdmin):
    list_display = ['person', 'discipline', 'course', 'fault_number']
    list_filter = ['course', 'discipline', 'person']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'shift']
    list_filter = ['shift']


@admin.register(Ocorrence)
class OcorrenceAdmin(admin.ModelAdmin):
    list_display = ['description', 'date', 'course', 'discipline', 'person']
    list_filter = ['course', 'discipline', 'person']
    date_hierarchy = 'date'


@admin.register(DisciplinesPerCourse)
class DisciplinesPerCourseAdmin(admin.ModelAdmin):
    list_display = ['course', 'discipline', 'shift', 'workload']
    list_filter = ['course', 'discipline', 'shift']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['person', 'discipline', 'avaliation', 'frequence']
    list_filter = ['discipline', 'avaliation', 'frequence']
