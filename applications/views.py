import base64
from io import BytesIO

import qrcode
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

from nubel_project.translations import tr, LANGS

from .forms import ApplicationForm
from .models import Application


def set_lang(request, code):
    """Store the chosen UI language (uz/ru) in the session and go back."""
    if code in LANGS:
        request.session["lang"] = code
    nxt = request.META.get("HTTP_REFERER", "/")
    if not url_has_allowed_host_and_scheme(
            nxt, allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        nxt = "/"
    return redirect(nxt)


def home_view(request):
    return render(request, "home.html")


@login_required
def application_create_view(request):
    lang = request.session.get("lang", "uz")
    # One application per user.
    if hasattr(request.user, "application"):
        messages.info(request, tr("msg.have_app", lang))
        return redirect("applications:receipt",
                        code=request.user.application.unique_code)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES, lang=lang)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, tr("msg.app_created", lang))
            return redirect("applications:receipt",
                            code=application.unique_code)
    else:
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "phone_number": request.user.phone_number,
        }
        form = ApplicationForm(initial=initial, lang=lang)
    return render(request, "applications/create.html", {"form": form})


def _qr_data_uri(text: str) -> str:
    qr = qrcode.QRCode(box_size=8, border=2,
                       error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#1b3a6b", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{encoded}"


@login_required
def receipt_view(request, code):
    application = get_object_or_404(Application, unique_code=code)
    # Only the owner or staff may see the receipt.
    if application.user != request.user and not request.user.is_staff:
        raise Http404
    verify_url = request.build_absolute_uri(
        reverse("applications:verify", args=[application.unique_code]))
    qr = _qr_data_uri(verify_url)
    return render(request, "applications/receipt.html", {
        "application": application,
        "qr": qr,
        "verify_url": verify_url,
    })


@login_required
def my_application_view(request):
    application = getattr(request.user, "application", None)
    if application is None:
        return redirect("applications:create")
    return redirect("applications:receipt", code=application.unique_code)


def verify_view(request, code):
    """Public status page reachable from the QR code."""
    application = get_object_or_404(Application, unique_code=code)
    return render(request, "applications/verify.html", {
        "application": application,
    })
