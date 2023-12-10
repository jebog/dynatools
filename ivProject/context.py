# ivelo/context_processors.py
def global_variables(request):
    # Define your global variables here
    if "ivelo" in request.path_info:
        return {
            'app_name': 'ivelo',
        }
    else:
        return {
            'app_name': '',
        }
