from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, 'app/index.html', {'employees': employees})


def add_update(request, emp_id=0):
    if emp_id:
        user = get_object_or_404(Employee, id=emp_id)
        form = EmployeeForm(request.POST or None, instance=user, initial={"user": user})

    else:
        form = EmployeeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)

            # Get the 'username' from the form
            # if not emp_id:
            username = request.POST.get('user')

            # Create the user with the 'username' as above which creates
            # the employee user as well. If the user exists, update the record
            if emp_id:
                user = User.objects.get(username=username)
                user.save()
            else:
                user = User.objects.create(username=username)

            # Now get the employee user and add/update the extra fields
            employee = Employee.objects.get(id=user.id)
            employee.address_1 = request.POST.get('address_1')
            employee.address_2 = request.POST.get('address_2')
            employee.city = request.POST.get('city')
            employee.state = request.POST.get('state')
            employee.zip = request.POST.get('zip')
            employee.save()

        # 'Employee' user saved - now redirect to index page
        return redirect('app:index')

    return render(request, 'app/add_update.html', {'form': form})
