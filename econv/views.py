from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from urllib.request import urlopen
import chardet

from econv.models import Codec


def index(request):
    return render(request, 'index.html', {'codecs': Codec.objects.all()})

@csrf_exempt
def conv(request):
    url = request.POST.get('url', None)
    text = request.POST.get('text', None)
    from_enc = request.POST.get('from', 'auto')
    to_enc = request.POST.get('to', 'utf_8')
    url_result = None
    text_result = None

    if url:
        response = urlopen(url)
        content = response.read()
        if from_enc == 'auto':
            from_enc = chardet.detect(content)['encoding']

        # if response.getheader('content_type') == 'text/html':
        #     url_result = content.decode(from_enc).encode(to_enc, 'xmlcharrefreplace')
        url_result = content.decode(from_enc).encode(to_enc, 'replace')
    if text:
        if from_enc == 'auto':
            from_enc = chardet.detect(text)['encoding']
        text_result = text.decode(from_enc).encode(to_enc, 'replace')

    return render(request, 'conv.html',
        {'url_result': url_result, 'text_result': text_result})
