from django.db import models


class Sprint(models.Model):
    sprint_number = models.IntegerField(primary_key=True)
    start_date = models.DateField(unique=True)
    end_date = models.DateField(unique=True)

    def __str__(self):
        return 'Sprint ' + str(self.sprint_number) + ' (' + str(self.start_date) + ' - ' + str(self.end_date) + ')'


class TaskType(models.Model):
    task_type = models.CharField(null=False, max_length=15, unique=True)

    def __str__(self):
        return self.task_type


class TaskCreator(models.Model):
    creator = models.CharField(null=False, max_length=15, unique=True)

    def __str__(self):
        return self.creator


class PRType(models.Model):
    pr_type = models.CharField(null=False, max_length=15, unique=True)

    def __str__(self):
        return self.pr_type


class Responsable(models.Model):
    name = models.CharField(unique=True, max_length=25)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_number = models.IntegerField(primary_key=True)
    task_url = models.TextField(unique=True, default='None')
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    type = models.ForeignKey(TaskType, default=2, on_delete=models.CASCADE)
    creator = models.ForeignKey(TaskCreator, default=2, on_delete=models.CASCADE)
    planned = models.BooleanField(default=True)
    added = models.BooleanField(default=False)
    db_issue = models.BooleanField(default=False)
    research = models.BooleanField(default=False)
    cancelled_resolved = models.BooleanField(default=False)
    duplicated = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    delivered_datetime = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return str(self.sprint) + ' - Task ' + str(self.task_number) + ' - ' + str(self.type)

    def get_task_number(self):
        return self.task_number


class PointingEnvironments(models.Model):
    point = models.CharField(unique=True, max_length=25)

    def __str__(self):
        return self.point


class PR(models.Model):
    pr_number = models.IntegerField(primary_key=True)
    task = models.ManyToManyField(Task)
    responsable = models.ForeignKey(Responsable, null=True, default=None, on_delete=models.CASCADE)
    type = models.ForeignKey(PRType, null=True, default=None, on_delete=models.CASCADE)
    point = models.ForeignKey(PointingEnvironments, null=True, default=1, on_delete=models.CASCADE)
    sent = models.BooleanField(default=True)
    merged = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    note = models.TextField(null=True, blank=True)
    rolled_back = models.BooleanField(default=False)
    still_open = models.BooleanField(default=False)
    send_datetime = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        tasks = Task(self.task.all()).get_task_number()

        return 'PR ' + str(self.pr_number) + ' Type: ' + str(self.type) + ' Task: ' + \
               str(list(tasks)) + ' Creator: ' + str(self.responsable)
