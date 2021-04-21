from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
from django.template import loader
import cgi, cgitb
# Create instance of FieldStorage



from script.client import *
from script.info import *

def ok(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        # import function to run


        # call function
        #form = cgi.FieldStorage()
        #file_name = form.getvalue('file_name')
        file_name = request.POST.get('file_name')
        file_n = file_name.split("/")
        print(file_n[0] +"adsfscf" + file_n[1])
        client = Client(file_n[0])
        client.download(file_n[1],file_n[3])
        #path="media/"+ str(file_n[3])
        f = "./script/uploaded_data.json"
        json_file = open(f, 'r')
        data = json.load(json_file)
        json_file.close()
        dictt = {}
        for a in data:
            for b in data[a]:
                dictt[data[a][b]] = b
        print(dictt)
        context = {'data': dictt}
        template = loader.get_template('Upload_down.html')


        # return user to required page
        return HttpResponse(template.render(context, request))

    if request.method == 'POST' and 'upload_run' in request.POST:
        # import function to run
        uploaded_file = request.FILES['myfile']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)


        # call function
        try:
            user_name = request.POST.get('user_name')
            if (len(user_name) == 0):
                user_name="anonymous"
            client = Client(user_name)
            client.upload("media/" + uploaded_file.name)
        except:
            user_name = "anonymous"
            client = Client(user_name)
            client.upload("media/" + uploaded_file.name)

        f = "./script/uploaded_data.json"
        json_file = open(f, 'r')
        data = json.load(json_file)
        json_file.close()
        dictt = {}
        for a in data:
            for b in data[a]:
                dictt[data[a][b]] = b
        print(dictt)
        context = {'data': dictt}
        template = loader.get_template('Upload_down.html')

        # return user to required page
        return HttpResponse(template.render(context, request))
    else:
        #return render(request,'Upload_down.html')
        f = "./script/uploaded_data.json"
        json_file = open(f, 'r')
        data = json.load(json_file)
        print(type(data))
        json_file.close()
        dictt={}
        for a in data:
            for b in data[a]:
                dictt[data[a][b]]=b
                #print(type(b))
        #print(dictt)
        context = {'data': dictt}
        print(context)
        template = loader.get_template('Upload_down.html')
        return HttpResponse(template.render(context, request))

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def signup(request):
    return render(request,'signup.html')
