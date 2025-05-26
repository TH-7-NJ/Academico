from django.contrib import admin
from .models import *

admin.site.register(Cidade)
admin.site.register(Turno)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(TipoAvaliacao)
admin.site.register(Pessoa)


# Ocupação e Pessoas
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [PessoaInline]

admin.site.register(Ocupacao,OcupacaoAdmin)

# Instituição e cursos
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [CursoInline]
admin.site.register(Instituicao,InstituicaoAdmin)

# Area do saber e Cursos
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [CursoInline]
admin.site.register(AreaSaber,AreaSaberAdmin)

# Cursos e Disciplinas
class DisciplinasInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [DisciplinasInline]

admin.site.register(Curso, CursoAdmin)

# Disciplina e Avaliações 
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [AvaliacaoInline]
admin.site.register(Disciplina,DisciplinaAdmin)

# Turmas e Alunos 
class AlunoInline(admin.TabularInline):
    model = Matricula
    extra = 1
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [AlunoInline]
admin.site.register(Turma,TurmaAdmin)
