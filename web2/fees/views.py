from django.shortcuts import render

# Create your views here.


def feesPage(request):

    fees={    
        'coursefees' : {
                'python': 5000,
                'django': 4000, 'html': 3000, 'css': 3000, 'js': 4500,
                'tailwind': 3999,   'bootstrap': 5399, 'c': 7399, 'c++': 4999,
                'c#': 4500,  'java': 3999, 'dsa':  5399,
        }
    }

    return render(request, 'fees/feePage.html', context=fees)
