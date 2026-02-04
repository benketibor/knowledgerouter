"""Simple health check endpoint for Render.com"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def healthz(request):
    """Health check endpoint - returns 200 OK"""
    return JsonResponse({'status': 'healthy'}, status=200)
