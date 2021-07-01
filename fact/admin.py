from django.contrib import admin
from .models import Sprint, Task, TaskType, TaskCreator, PRType, PR

admin.site.register(Sprint)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ['task_number']
    search_fields = ['task_number']
    list_filter = ['sprint', 'type', 'creator', 'planned', 'added', 'db_issue', 'research', 'cancelled_resolved',
                   'delivered', 'delivered_datetime']


admin.site.register(TaskType)
admin.site.register(TaskCreator)
admin.site.register(PRType)
admin.site.register(PR)
