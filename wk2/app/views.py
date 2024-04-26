from django.shortcuts import render, HttpResponseRedirect

# Create your views here.


def delete_data(request, id):
    if request.method == "POST":
        dt = student.object.get(pk=id)
        dt.delete()
        return HttpResponseRedirect("/")
    pass
