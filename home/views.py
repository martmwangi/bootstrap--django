from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def moh(request):
    return render(request, 'moh.html', {})


def capitalize(request):

    return render(request, 'capitalize.html', {})

"""    def cap(str):
        str = input("Enter your statement: ")
    new_str = str.split()
    final_str = []
    for i in new_str:
        final_str.append(i.replace(i[0], i[0].upper()))
    return ' '.join(final_str)
print (cap(str))
"""
