from django.shortcuts import  render
def upload_page(request):
    return render(request, "fileupload/uploadpage.html")