from django.shortcuts import render

# Create your views here.


def template(request):
    # return render(request, 'app/base.html', {'key': name})
    student = {
        'std': ['Ram', 'Hari', 'Divas']
    }
    return render(request, 'app/base.html', student)
