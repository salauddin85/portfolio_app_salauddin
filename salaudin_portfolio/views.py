from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import SalauddinPortfolio
from .serializers import SalauddinPortfolioSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class SalauddinPortfolioCreateView(viewsets.ModelViewSet):
    queryset = SalauddinPortfolio.objects.all()
    serializer_class = SalauddinPortfolioSerializer

    def perform_create(self, serializer):
        # Save the new portfolio instance
        portfolio_instance = serializer.save()

        # Send email notification
        self.send_notification_email(portfolio_instance)

    def send_notification_email(self, portfolio_instance):
        email_subject = portfolio_instance.subject  # Use the subject from the form
        email_body = render_to_string("portfolio_email.html", {
            'name': portfolio_instance.name,
            'email': portfolio_instance.email,
            'subject': portfolio_instance.subject,
            'message': portfolio_instance.message,
        })

        # Replace 'your_recipient_email@example.com' with the actual recipient's email
        recipient_email = 'ahmedsalauddin677785@gmail.com'
        
        email = EmailMultiAlternatives(email_subject, '', to=[recipient_email])
        email.attach_alternative(email_body, 'text/html')
        email.send()

    def create(self, request, *args, **kwargs):
        # Override the create method to handle unauthenticated users
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return SalauddinPortfolio.objects.all()
