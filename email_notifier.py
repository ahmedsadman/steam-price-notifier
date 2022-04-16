import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Email:
    api_key = os.environ.get('SENDGRID_API_KEY')

    @classmethod
    def send(cls, subject, content):
        message = Mail(
            from_email=os.environ.get('FROM_EMAIL'),
            to_emails=os.environ.get('TO_EMAIL'),
            subject=subject,
            html_content=content)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(message)
        except Exception as e:
            print('Error occured while sending email', e.message)

    @classmethod
    def notify_price_drop(cls, name, formatted_price):
        subject = f'Steam Discount: Get {name} with only {formatted_price} today!'
        content = f'''
        <div>
        Hey Ahmed,<br/><br/>
        This is to inform you that the price of {name} just dropped to <strong>{formatted_price}</strong>. Grab it while you can.<br/><br/>
        Sincerely,<br/>
        Your Humble Steam Notifier
        </div>
        '''

        cls.send(subject, content)
    