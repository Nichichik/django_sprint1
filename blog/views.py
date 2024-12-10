from django.shortcuts import render

# Временный список постов
posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море...'''
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел...'''
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный...'''
    },
]


def index(request):
    return render(request, 'html/index.html', {'posts': posts})


def post_detail(request, id):
    post = next((p for p in posts if p['id'] == id), None)
    return render(request, 'html/detail.html', {'post': post})


def category_posts(request, category_slug):
    return render(request, 'html/category.html', {'category_slug': category_slug})

