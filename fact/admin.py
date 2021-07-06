from django.contrib import admin
from .models import Sprint, Task, TaskType, TaskCreator, PRType, PR, Responsable


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ['task_number']
    search_fields = ['task_number']
    list_filter = ['sprint', 'type', 'creator', 'planned', 'added', 'db_issue', 'research', 'cancelled_resolved',
                   'delivered', 'delivered_datetime']


@admin.register(PR)
class PRAdmin(admin.ModelAdmin):
    ordering = ['pr_number']
    search_fields = ['pr_number']
    list_filter = ['task__sprint', 'type', 'responsable', 'sent', 'closed', 'merged', 'rolled_back', 'still_open']


admin.site.register(TaskType)
admin.site.register(TaskCreator)
admin.site.register(PRType)
admin.site.register(Sprint)
admin.site.register(Responsable)
