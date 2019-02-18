from django.shortcuts import render

from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects.all()
    portfolio_groups = []

    i = 0
    temp = portfolios[0:4]
    while temp:
        portfolio_groups.append(temp)
        i += 4
        temp = portfolios[i:i+4]
    
    portfolio_dic = {
        'portfolio_groups': portfolio_groups,
        'portfolios': portfolios,
        'activate': 'portfolio'
        }
    return render(request, 'portfolio/portfolio.html', portfolio_dic)