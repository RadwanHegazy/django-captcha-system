from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .captcha import Captcha
from uuid import uuid4
import requests
import urllib.request 
from .models import ImageModel
from io import BytesIO
from django.core.files import File



def home (request) : 
    return render(request,'index.html')


def create_session (request) : 

    req = requests.get('https://random.responsiveimages.io/v1/docs',allow_redirects=True)

    img_url = req.url
    img_name = f"media/downloaded-images/{uuid4()}.png"
    urllib.request.urlretrieve( 
        img_url,
        img_name
      ) 
    
    

    cap = Captcha(img_path=img_name)

    
    img = ImageModel.objects.create(
        info = f'{cap.info()}',
        uuid = uuid4(),
    )
    img_name = f'{uuid4()}.png'

    while True :
        try : 
            blob_for_big = BytesIO()
            cap.original_image.save(blob_for_big, 'PNG')
            img.big_image.save(img_name,File(blob_for_big),save=False)
        
            blob_for_small = BytesIO()
            cap.object.save(blob_for_small, 'PNG')
            img.small_image.save(img_name,File(blob_for_small),save=False)
            
            img.save()
            break
        except SystemError :
            pass


    session = img.uuid
    return redirect('session',session)

def session (request, sessionuuid) :
    session = get_object_or_404(ImageModel, uuid=sessionuuid)
    session_info = session.get_info_as_dict()

    context = {
        'session' : session,
        'object_width' : session_info['object_width'],
        'object_height' : session_info['object_height'],
    }

    if request.method == "POST" : 
        user_x = request.POST['user_x'] 
        user_y = request.POST['user_y']

        user_x = int(user_x)
        user_y = int(user_y)

        correct_x = session_info['object_x']
        is_correct_x  = bool(user_x in range(correct_x[0], correct_x[1]))


        correct_y = session_info['object_y']
        is_correct_y = bool(user_y in range(correct_y[0], correct_y[1]))

        if is_correct_x and is_correct_y :
            context['state'] = 'valid'
            context['x'] = f"{user_x}px"
            context['y'] = f"{user_x}px"
        else:
            context['state'] = 'invalid'

    
    return render(request,'capthca.html',context)