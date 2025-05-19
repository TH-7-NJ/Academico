from django.contrib import admin
from .models import *

class PersonInline(admin.TabularInline):
    model = Person 
    extra = 3

class OccupationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

    inlines = [PersonInline]

class CourseInline(admin.TabularInline):
    model = Course
    extra = 3

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

    inlines = [CourseInline]

class KnowledgeAreaAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

    inlines = [CourseInline]

class AvaliationInline(admin.TabularInline):
    model = Avaliation
    extra = 3

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("name", "name",)
    search_fields = ("name", "name",)

    inlines = [AvaliationInline, CourseInline]

class SessionInline(admin.TabularInline):
    model = Session
    extra = 3

class UfInline(admin.TabularInline):
    model = Uf
    extra = 3

class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

    inlines = [UfInline]

class FrequenceInline(admin.TabularInline):
    model = Frequence
    extra = 3

class DisciplineInline(admin.TabularInline):
    model = Discipline
    extra = 3

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "name","name", "name", "name",)
    search_fields = ("name", "name","name", "name", "name",)

    inlines = [SessionInline, CourseInline, DisciplineInline, AvaliationInline, FrequenceInline]

admin.site.register(Occupation, OccupationAdmin)
admin.site.register(EducationalInstitution, InstitutionAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(City, CityAdmin)