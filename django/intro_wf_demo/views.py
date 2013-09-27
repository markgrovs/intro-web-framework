from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

@render_to('intro_wf_demo:home.html')
@login_required
def home(request):
    return {
        "message": "Hello World from intro_wf_demo!",
        "app_name": "intro_wf_demo"
    }