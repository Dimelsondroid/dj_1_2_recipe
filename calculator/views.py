from django.http import HttpResponse
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
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'borsch': {
        'свекла, шт': 3,
        'капуста, качан': 0.75,
        'мясо, кг': 0.5,
        'помидор, шт': 2,
    },
}


def get_recipe(request, dish):
    servings = int(request.GET.get('servings', 1))
    per_serving = {}
    for ingredient, amount in DATA[dish].items():
        per_serving[ingredient] = round(servings*amount, 2)
    context = {'recipe': per_serving}
    return render(request, 'calculator/index.html', context)
