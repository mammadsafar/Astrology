from django.shortcuts import render

from .models import Card, SocialMedia, Button


def business_card(request, slug):
    print(slug)
    data = Card.objects.filter(slug=slug).first()
    print(data)
    social_media = SocialMedia.objects.filter(card=data)
    button = Button.objects.filter(card=data)

    btn_len = button.count()
    btn_text = ''
    for i in range(0, btn_len, 2):
        btn_text += '<div class="row">'

        btn_text += f'<a href="{button[i].link}" class="btn col button_link">{button[i].text}</a>'

        if btn_len % 2 != 0 and i+1 == btn_len:
            pass
        else:
            btn_text += f'<a href="{button[i+1].link}" class="btn col button_link">{button[i+1].text}</a>'

        btn_text += '</div>'


    context = {
        'page_title': data.page_title,
        'meta_description': 'data.meta_description',
        'meta_link': data.id,
        'logo': data.logo,
        'image': data.image,
        'first_name': data.first_name,
        'Last_name': data.last_name,
        'about_me': data.title,
        'socialmedias': social_media,
        'buttons': btn_text,
    }

    return render(request, 'card.html', context)
