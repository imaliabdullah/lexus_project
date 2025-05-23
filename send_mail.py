import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    # Looking to send emails in production? Check out our Email API/SMTP product!
    smtp_server='sandbox.smtp.mailtrap.io'
    port = 2525
    login = '4aa9471e8f2dad'
    password = '4b0a606d90fb82'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())