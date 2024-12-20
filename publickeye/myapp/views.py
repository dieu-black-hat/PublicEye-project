from django.shortcuts import render
from .forms import CrimeReportForm  # Import your form from myapp
from .models import CrimeReport  # Import your CrimeReport model

def hello(request):
    return render(request, "hello.html")

def index(request):
    total_reports = CrimeReport.objects.count()  # Get the total number of reports
    total_openreports = CrimeReport.objects.filter(status="open").count()  # Filter reports with status 'open'
    total_resolvedreports = CrimeReport.objects.filter(status="resolved").count()
    context = {
        'total_reports': total_reports,
        'total_openreports': total_openreports,
        'total_resolvedreports': total_resolvedreports,
    }
    return render(request, 'mywebapp/index.html', context)
def about(request):
    return render(request, 'mywebapp/about.html')


def services(request):
    return render(request, 'mywebapp/services.html')

def otp_verification(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if str(entered_otp) == str(request.session.get('otp')):
            # Clear the OTP from the session
            del request.session['otp']
            return redirect('report_crime')  # Redirect back to the report crime page
        else:
            return render(request, 'mywebapp/otp_verification.html', {'error': 'Invalid OTP'})

    return render(request, 'mywebapp/otp_verification.html')

from django.shortcuts import render
from .models import MostWanted

def mwanted(request):
    wanted_list = MostWanted.objects.all()  # Get all Most Wanted entries
    return render(request, 'mywebapp/mwanted.html', {'wanted_list': wanted_list})

def success(request):
    return render(request, 'mywebapp/success_page.html')

def submit_user_info(request):
    return render(request, 'mywebapp/submit_user_info.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CrimeReportForm  # Make sure to import your form
from .models import CrimeReport, Notification  # Import your models
import random
from django.core.mail import send_mail

def generate_otp():
    return random.randint(100000, 999999)

def send_otp_email(email, otp):
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp}',
        'dieudonnebyiringiro2020@gmail.com',  # Replace with your email
        [email],
        fail_silently=False,
    )

def report_crime(request):
    success_message = None  # Initialize success message
    if request.method == 'POST':
        form = CrimeReportForm(request.POST, request.FILES)
        email = request.POST.get('email')  # Get email from the form

        # Check if user exists
        user_exists = CrimeReport.objects.filter(email=email).exists()

        if user_exists:
            # Generate and send OTP for returning users
            otp = generate_otp()
            request.session['otp'] = otp
            send_otp_email(email, otp)
            return redirect('otp_verification')  # Redirect to OTP verification page
        else:
            if form.is_valid():
                # Save the report
                report = form.save(commit=False)  # Save without committing yet
                
                # Create a notification for the user
                reporter_name = request.user.get_full_name() or request.user.username  # Get the reporter's name
                Notification.objects.create(
                    user=request.user,
                    message=f"{reporter_name}, your crime report has been submitted successfully."
                )
                
                report.save()  # Now save the report to the database
                
                success_message = "Thank you! Your report has been submitted successfully and you will receive a case code via phone message."
                form = CrimeReportForm()  # Reset the form after successful submission
    else:
        form = CrimeReportForm()
        
    return render(request, 'mywebapp/report_crime.html', {'form': form, 'success_message': success_message})
from django.shortcuts import render
from .models import CrimeReport

def indexdashboard(request):
    total_reports = CrimeReport.objects.count()  # Get the total number of reports
    total_openreports = CrimeReport.objects.filter(status="open").count()  # Filter reports with status 'open'
    total_resolvedreports = CrimeReport.objects.filter(status="resolved").count()
    context = {
        'total_reports': total_reports,
        'total_openreports': total_openreports,
        'total_resolvedreports': total_resolvedreports,
    }
    return render(request, 'mywebapp/indexdashboard.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import CrimeReport, Comment, Feedback  # Ensure Feedback is imported
from django.contrib import messages

def openreports(request, id):
    report = get_object_or_404(CrimeReport, id=id)
    feedbacks = Feedback.objects.filter(report=report)  # Fetch feedback for the specific report

    if request.method == 'POST':
        # Create a new Comment instance
        comment = Comment(
            report=report,
            officer_email=request.POST['officer_email'],
            comment_text=request.POST['comment'],
            status='pending',  # Set default status or handle as needed
            evidence_collected=request.POST.get('evidence', ''),
        )

        # Handle file uploads if needed
        if 'suspect_image' in request.FILES:
            comment.attachments = request.FILES['suspect_image']  # Save uploaded image

        comment.save()  # Save the Comment to the database
        messages.success(request, 'Comment submitted successfully.')
        return redirect('openreports', id=report.id)  # Redirect to the updated report view

    return render(request, 'mywebapp/openreports.html', {
        'report': report,
        'feedbacks': feedbacks,  # Pass feedbacks to the template
    })
def resolvedreports(request):
    return render(request, 'mywebapp/resolvedreports.html')

from django.shortcuts import render, redirect
from .models import Feedback, CrimeReport
from django.contrib import messages

# myapp/views.py
from django.shortcuts import render, redirect
from .models import Feedback, CrimeReport
from django.contrib import messages

def feedback(request):
    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        latitude = request.POST.get('latitude')  # Get latitude
        longitude = request.POST.get('longitude')  # Get longitude

        # Check if the report exists
        try:
            report = CrimeReport.objects.get(id=report_id)
            Feedback.objects.create(
                report=report,
                email=email,
                subject=subject,
                message=message,
                latitude=latitude,  # Store latitude
                longitude=longitude  # Store longitude
            )
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('feedback')
        except CrimeReport.DoesNotExist:
            messages.error(request, 'Invalid Report ID. Please check and try again.')

    return render(request, 'mywebapp/feedback.html')

def totalreports(request):
    reports = CrimeReport.objects.all()  # Fetch all crime reports from the CrimeReport model
    return render(request, 'mywebapp/totalreports.html', {'reports': reports})

def notifications(request):
    return render(request, 'mywebapp/notifications.html')
from django.shortcuts import render, get_object_or_404
from .models import CrimeReport  # Make sure to import your CrimeReport model

from django.shortcuts import render, get_object_or_404
from .models import CrimeReport  # Make sure to import your CrimeReport model

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import CrimeReport, Comment
from weasyprint import HTML
from django.template.loader import render_to_string

def requestreport(request):
    report = None
    invalid_report = False  # Flag to indicate if the report ID is invalid
    report_id = request.GET.get('report_id')

    if report_id:
        try:
            report = CrimeReport.objects.get(id=report_id)  # Fetch the CrimeReport using the ID
            comments = Comment.objects.filter(report=report)  # Get comments related to the report
            
            if request.GET.get('generate_pdf') == 'true':
                # Render the report details and comments to an HTML template
                html_string = render_to_string('mywebapp/requestreport.html', {'report': report, 'comments': comments})
                
                # Convert HTML to PDF
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="report_{report_id}.pdf"'
                HTML(string=html_string).write_pdf(response)
                return response

        except CrimeReport.DoesNotExist:
            invalid_report = True  # Set the flag if the report does not exist

    return render(request, 'mywebapp/requestreport.html', {
         'report': report,
    'comments': comments,  # Ensure this matches what you're using in the template
    'invalid_report': invalid_report,
})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def loginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('totalreports')  # Redirect to the total reports page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'mywebapp/loginform.html')
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('index')  # Redirect to the index page