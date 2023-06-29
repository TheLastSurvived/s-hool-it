from django.contrib import admin

from .models import Answer, Question, Quiz, User, Subject, Theory, Student, TakenQuiz


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Theory)
admin.site.register(Student)
admin.site.register(TakenQuiz)