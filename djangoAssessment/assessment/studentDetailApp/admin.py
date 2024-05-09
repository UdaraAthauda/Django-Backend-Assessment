from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Student, ImportExportModelAdmin)
admin.site.register(School, ImportExportModelAdmin)
admin.site.register(Class, ImportExportModelAdmin)
admin.site.register(AssessmentAreas, ImportExportModelAdmin)
admin.site.register(Answers, ImportExportModelAdmin)
admin.site.register(Awards, ImportExportModelAdmin)
admin.site.register(Subject, ImportExportModelAdmin)
admin.site.register(Alldata, ImportExportModelAdmin)