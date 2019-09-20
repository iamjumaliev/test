from django.shortcuts import render,get_object_or_404,redirect

from webapp.forms import PlanForm
from webapp.models import Plan,STATUS_CHOICES


def index_view(request, *args, **kwargs):
    plans = Plan.objects.all()
    return render(request, 'index.html', context={
        'plans': plans
    })


def plan_view(request,pk):
    plan = get_object_or_404(Plan, pk=pk)
    return render(request, 'plan.html', context={
        'plan': plan
    })

def add_new_plan(request, *args, **kwargs):

    if request.method == 'GET':

        form = PlanForm()

        return render(request, 'create.html', context={'form': form})

    elif request.method == 'POST':

        form = PlanForm(data=request.POST)

        if form.is_valid():

            plan = Plan.objects.create(

                description=form.cleaned_data['description'],

                status=form.cleaned_data['status'],

                deadline=form.cleaned_data['deadline'],

                full_description=form.cleaned_data['full_description']

            )

            return redirect('plan_view', pk=plan.pk)

        else:

            return render(request, 'create.html', context={'form': form})



def plan_update_view(request, pk):

        plan = get_object_or_404(Plan, pk=pk)

        if request.method == 'GET':

            form = PlanForm(data={

                'description': plan.description,

                'status': plan.status,

                'deadline': plan.deadline,

                'full_description': plan.full_description

            })

            return render(request, 'update.html', context={'form': form, 'plan': plan})

        elif request.method == 'POST':

            form = PlanForm(data=request.POST)

            if form.is_valid():

                plan.description = form.cleaned_data['description']

                plan.status = form.cleaned_data['status']

                plan.deadline = form.cleaned_data['deadline']

                plan.full_description = form.cleaned_data['full_description']

                plan.save()

                return redirect('plan_view', pk=plan.pk)

            else:

                return render(request, 'update.html', context={'form': form, 'plan': plan})


def plan_delete_view(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'plan': plan})
    elif request.method == 'POST':
        plan.delete()
        return redirect('index')







