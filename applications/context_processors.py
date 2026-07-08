def language(request):
    """Expose the active language code (uz/ru) to every template."""
    return {"LANG": request.session.get("lang", "uz")}
