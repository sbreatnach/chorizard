from django.views.generic import TemplateView
from django.shortcuts import redirect

from chorizard.chores.forms import NewChoreForm


class HomeView(TemplateView):
    template_name = "home.html.j2"
    http_method_names = ["get", "post"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["families"] = self.request.user.families.all()
        context["show_new_chore"] = self.request.GET.get("show_new_chore", "") != ""
        return context

    def get(self, request, *_args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["chore_form"] = NewChoreForm()
        return self.render_to_response(context)

    def post(self, request, *_args, **kwargs):
        form = NewChoreForm(request.POST)
        if form.is_valid():
            return redirect("home")
        context = self.get_context_data(**kwargs)
        context["chore_form"] = form
        return self.render_to_response(context)
