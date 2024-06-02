from django.shortcuts import redirect, render
from curd_app.models import Tbl_Employee

# Create your views here.

def create(request):
    if request.method == 'POST':
        # Code for save date
        
        e_name = request.POST.get('emp_name')
        e_email = request.POST.get('emp_email')
        e_mobile = request.POST.get('mobile')
        qs = Tbl_Employee.objects.create(name = e_name, email = e_email, mobile_no = e_mobile)
        print(qs.id)
        if qs:
            return redirect('/retrive/')
    else:    
        return render(request, 'create_emp.html') 

def retrive_all_emp(request):
    qs = Tbl_Employee.objects.all()

    context = {
        'emp_data':qs
        }
    return render(request, 'retrive.html', context)

def delete_emp(request, emp_id):
    qs = Tbl_Employee.objects.filter(id=emp_id).delete()

    if qs:         
        return redirect('/retrive/')

def update_emp(request, emp_id):
    if request.method == 'POST':
        #print(request.POST)
        e_name = request.POST.get('emp_name')
        e_email = request.POST.get('emp_email')
        e_mobile = request.POST.get('mobile')
        qs = Tbl_Employee.objects.filter(id=emp_id).update(name = e_name, email = e_email, mobile_no = e_mobile)
        if qs:
            return redirect('/retrive/')

    else:    
        qs = Tbl_Employee.objects.get(id=emp_id)
        return render(request, 'update.html', {'emp_update_data': qs})        
