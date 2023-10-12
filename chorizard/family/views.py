from django.shortcuts import render


def manage(request):
    context = {
        "families": request.user.families.all(),
    }
    return render(request, "manage.html.j2", context=context)
