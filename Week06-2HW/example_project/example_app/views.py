from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    text_len = len(text)
    semi_text = text.replace(" ", "")
    rmv_len = len(semi_text)

    if text == '':
        word_num = 0
    else:
        word_num = text.count(" ")+1        



    return render(request, "result.html", {
        'total_len' : text_len,
        'just': text,
        "rmv_len" : rmv_len,
        "word_num" : word_num
    })