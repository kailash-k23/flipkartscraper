import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def mailto(to_address, file_attachment):                
    from_address = "mail.test.fe@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = 'Details of the product Enquired'
    body = "You can find the details of the product that you enquired from flipkart, in the file attached to this mail."
    msg.attach(MIMEText(body, 'plain'))

    filename = str(file_attachment)
    attach = open(file_attachment, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attach).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(from_address, 'kailash123')

    text = msg.as_string()

    s.sendmail(from_address, to_address, text)

    s.quit()



