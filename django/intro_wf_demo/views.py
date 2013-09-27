from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

@render_to('intro_wf_demo:home.html')
@login_required
def home(request):
    return {
        "message": "Hello World from intro_wf_demo!",
        "app_name": "intro_wf_demo"
    }

# @render_to('intro_wf_demo:custom_viz.html')
# @login_required
# def custom_viz(request):
#   return {
#     "app_name": "intro_wf_demo"
#   }


@render_to()
@login_required
def render_page(request, tmpl):
    return {
      "TEMPLATE": "intro_wf_demo:%s.html" % tmpl
    }