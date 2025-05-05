from django.shortcuts import render

from django.shortcuts import render
from .models import PortfolioEntry

def save_portfolio(request):
    if request.method == 'POST':
        # Get data from HTML form
        full_name = request.POST.get('full_name')
        job_title = request.POST.get('job_title')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        website = request.POST.get('website')
        summary = request.POST.get('summary')

        # Save into database
        PortfolioEntry.objects.create(
            full_name=full_name,
            job_title=job_title,
            email=email,
            phone=phone,
            location=location,
            website=website,
            summary=summary
        )

        return render(request, 'portfolio/success.html')  # Show Thank You page
    return render(request, 'portfolio/portfolio_form.html')


