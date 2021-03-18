from django.shortcuts import render,get_object_or_404,redirect
from .models import Cat
from django.http import HttpResponse
import csv

def cat_list(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    cat = Cat.objects.all()

    return render(request, 'back/cat_list.html', {'cat':cat})


def cat_add(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    if request.method == "POST":
        name = request.POST.get('name')

        if name == "":
            error = "All Fields are required"
            return render(request, 'back/error.html', {'error':error})

        if len(Cat.objects.filter(name=name)) != 0:
            error = "Category Exist"
            return render(request, 'back/error.html', {'error':error})



        b = Cat(name=name)
        b.save()
        return redirect('cat_list')


    return render(request, 'back/cat_add.html')


def export_cat_csv(request):

    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="cat.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Count'])
    for i in Cat.objects.all():
        writer.writerow([i.name, i.count])





    return response




def import_csv(request):


    if request.method == 'POST':
        csv_file = request.FILES['csv_file']

        if not csv_file.name.endswith('.csv'):
            error = "Please Upload CSV file"
            return render(request, 'back/error.html', {'error':error})

        if not csv_file.multiple_chunks():
            error = "Please Upload CSV file"
            return render(request, 'back/error.html', {'error':error})










        file_data = csv_file.read().decode('utf-8')
        lines = file_data.split('\n')

        for line in lines :
            fields = line.split(',')

            try:
                if len(Cat.objects.filter(name=fields[0])) ==0 and fields[0] != 'Name' and fields[0] != '':
                    b = Cat(name=fields[0])
                    b.save()


                print(fields[0],fields[1])
            except:
                print('Finished')

    return redirect('cat_list')






