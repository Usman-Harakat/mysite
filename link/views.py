from django.http import HttpResponse

# Create your views here.
def link(request):
    try:
        Req_1 = str(request)
        Req_2 = Req_1.index("dob")
        Req_3 = Req_1[Req_2:]
        Req_4 = Req_3.index("'>")
        Req_5 = Req_3[:Req_4]
        Req_6 = Req_5.replace("/","")
        if "&" in Req_6:
            Req_7 = Req_6.index("&")
            Req_6 = Req_6[:Req_7]
        Link = "http://goodbooy.pythonanywhere.com/"+Req_6#رابط التحويل
        return HttpResponse('<img style="width: 400px;height: 144px;display: block;margin-left: auto;margin-right: auto;" src="https://msry.org/wp-content/uploads/%D8%A7%D8%B3%D8%AA%D8%BA%D9%81%D8%B1-%D8%A7%D9%84%D9%84%D9%87-%D8%A7%D9%84%D8%B9%D8%B8%D9%8A%D9%85.gif"><META HTTP-EQUIV="Refresh" CONTENT="0;URL={}">'.format(Link))
    except:
        Link = "https://www.google.com/"#رابط التوهيم
        return HttpResponse('<img style="width: 400px;height: 144px;display: block;margin-left: auto;margin-right: auto;" src="https://msry.org/wp-content/uploads/%D8%A7%D8%B3%D8%AA%D8%BA%D9%81%D8%B1-%D8%A7%D9%84%D9%84%D9%87-%D8%A7%D9%84%D8%B9%D8%B8%D9%8A%D9%85.gif"><META HTTP-EQUIV="Refresh" CONTENT="0;URL={}">'.format(Link))