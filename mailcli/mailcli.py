import argparse
import smtplib
import sys
from email.mime.text import MIMEText
from mailcli.__about__ import __version__

MAILGUN_SERVER = "smtp.mailgun.org"


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Mail-CLI, send mail with mailgun service.')

    parser.add_argument(
        '-V', '--version', dest='version', action='store_true', help="show version")
    parser.add_argument(
        '-u', '--mailgun-smtp-username', help="Specify mailgun smtp username.")
    parser.add_argument(
        '-p', '--mailgun-smtp-password', help="Specify mailgun smtp password.")
    parser.add_argument(
        '--mail-sender', help="Specify email sender.")
    parser.add_argument(
        '--mail-recepients', nargs='*', help="Specify email recepients.")
    parser.add_argument(
        '--mail-subject', help="Specify email subject.")
    parser.add_argument(
        '--mail-content', help="Specify email content.")
    parser.add_argument(
        '--mail-content-path', help="Load file content as mail content.")

    args = parser.parse_args()
    if args.version:
        print("mail-cli version: {}".format(__version__))
        sys.exit(0)

    if not (args.mailgun_smtp_username and args.mailgun_smtp_password and \
            args.mail_sender and args.mail_recepients):
        print("mailgun account configuration incomplete, exit.")
        sys.exit(1)

    if not args.mail_subject:
        print("mail subject missing, exit.")
        sys.exit(1)

    if not (args.mail_subject or args.mail_content_path):
        print("mail content missing, exit.")
        sys.exit(1)

    return args


def __load_file_content(file_path):
    """ Load file content as mail content.
    """
    with open(file_path) as f:
        return f.read()


def send_mail(args):
    """ send mail with SMTP.
        For more details, please check: https://documentation.mailgun.com/en/latest/quickstart-sending.html#send-via-smtp
    """
    try:
        mail_client = smtplib.SMTP(MAILGUN_SERVER, 587)
        mail_client.login(args.mailgun_smtp_username, args.mailgun_smtp_password)

        mail_content = args.mail_content or __load_file_content(args.mail_content_path)
        msg = MIMEText(mail_content, _subtype='html', _charset='utf-8')
        msg["Subject"] = args.mail_subject
        msg["From"] = args.mail_sender
        msg["To"] = ";".join(args.mail_recepients)

        mail_client.sendmail(
            msg["From"],
            args.mail_recepients,
            msg.as_string()
        )
        mail_client.quit()
        print("Email sent")
    except Exception as e:
        print("SMTP Failed!!!")
        print(str(e))


def main():
    send_mail(arg_parser())


if __name__ == '__main__':
    main()
