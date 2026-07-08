from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from nubel_project.translations import tr
from .forms import RegisterForm, LoginForm, ProfileForm


def _lang(request):
    return request.session.get("lang", "uz")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")
    lang = _lang(request)
    if request.method == "POST":
        form = RegisterForm(request.POST, lang=lang)
        if form.is_valid():
            user = form.save(commit=False)
            user.phone_number = form.cleaned_data["phone_number"]
            user.is_phone_verified = True  # verification disabled for now
            user.save()
            login(request, user)
            messages.success(request, tr("msg.registered", lang))
            return redirect("accounts:profile")
    else:
        form = RegisterForm(lang=lang)
    return render(request, "accounts/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["lang"] = self.request.session.get("lang", "uz")
        return kwargs

    def get_success_url(self):
        return reverse_lazy("accounts:profile")

    def form_valid(self, form):
        messages.success(self.request, tr("msg.logged_in", _lang(self.request)))
        return super().form_valid(form)


def logout_view(request):
    lang = _lang(request)
    logout(request)                 # flushes the session
    request.session["lang"] = lang  # keep the chosen language
    messages.info(request, tr("msg.logged_out", lang))
    return redirect("home")


@login_required
def profile_view(request):
    application = getattr(request.user, "application", None)
    return render(request, "accounts/profile.html", {
        "profile_user": request.user,
        "application": application,
    })


@login_required
def profile_edit_view(request):
    lang = _lang(request)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user, lang=lang)
        if form.is_valid():
            form.save()
            messages.success(request, tr("msg.profile_updated", lang))
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user, lang=lang)
    return render(request, "accounts/profile_edit.html", {"form": form})
