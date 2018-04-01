from django import forms
from .models import Task
from .models import Project
from django.contrib.auth.models import User

status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)


class TaskRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    status = forms.ChoiceField(choices=status)
    due = forms.ChoiceField(choices=due)

    # def __init__(self, *args, **kwargs):
    #     if kwargs.get('instance'):
    #         initial = kwargs.setdefault('initial', {})
    #         initial['toppings'] = [t.pk for t in kwargs['instance'].topping_set.all()]
    #     forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model = Task
        fields = '__all__'


    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.due = self.cleaned_data['due']
        task.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            task.assign.add((assign))

        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Email'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'City'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Found date'