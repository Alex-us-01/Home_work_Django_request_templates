from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet_view(request):
    servings = request.GET.get('servings')
    if servings != None:
        recipe_dict = {}
        for key, value in DATA['omlet'].items():
            recipe_dict[key] = value * int(servings)

        context = {'recipe': recipe_dict}
        return render(request, 'calculator/index.html', context=context)
    else:
        context = {
            'recipe': DATA['omlet']
        }
        return render(request, 'calculator/index.html', context=context)


def pasta_view(request):
    servings = request.GET.get('servings')

    if servings != None:
        recipe_dict = {}
        for key, value in DATA['pasta'].items():
            recipe_dict[key] = value * int(servings)

        context = {'recipe': recipe_dict}
        return render(request, 'calculator/index.html', context=context)
    else:
        context = {
            'recipe': DATA['pasta']
        }
        return render(request, 'calculator/index.html', context=context)


def sandwich_view(request):
    servings = request.GET.get('servings')
    if servings != None:
        recipe_dict = {}
        for key, value in DATA['sandwich'].items():
            recipe_dict[key] = value * int(servings)

        context = {'recipe': recipe_dict}
        return render(request, 'calculator/index.html', context=context)
    else:
        context = {
            'recipe': DATA['sandwich']
        }
        return render(request, 'calculator/index.html', context=context)
