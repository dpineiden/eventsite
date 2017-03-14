from django.conf import settings

def site_data(request):
    return {'SITE_NAME':settings.SITE_NAME}
