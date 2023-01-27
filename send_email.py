import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "neoveta@gmail.com"
    password = "cewswxecyskdaanc"

    receiver = "neoveta@gmail.com"
    context = ssl.create_default_context()

    message = """\
    Subject : Hi 
    """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

