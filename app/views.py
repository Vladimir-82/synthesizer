from gtts import gTTS
from playsound import playsound
from django.shortcuts import render


LANGUAGE = 'en'


def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        obj = gTTS(text=action, lang=LANGUAGE, slow=False)
        obj.save("answer.mp3")
        playsound("answer.mp3")
        context = {"answer": True}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": ""}
        return render(request, 'app/index.html', context=context)