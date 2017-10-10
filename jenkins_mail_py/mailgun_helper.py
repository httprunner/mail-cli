import argparse
import sys
import requests
import smtplib
from email.mime.text import MIMEText
from . import __version__


class MailgunHelper(object):

    def __init__(self, parser=None):
        """
        """
        parser = parser or argparse.ArgumentParser(
            description='Mailgun helper, send mail with mailgun service.')

        parser.add_argument(
            '--mailgun-smtp-username', help="Specify mailgun smtp username.")
        parser.add_argument(
            '--mailgun-smtp-password', help="Specify mailgun smtp password.")
        parser.add_argument(
            '--mail-sender', help="Specify email sender.")
        parser.add_argument(
            '--mail-recepients', nargs='*', help="Specify email recepients.")
        parser.add_argument(
            '--mail-subject', help="Specify email subject.")
        parser.add_argument(
            '--mail-content', help="Specify email content.")
        parser.add_argument(
            '--jenkins-job-name', help="Specify jenkins job name.")
        parser.add_argument(
            '--jenkins-job-url', help="Specify jenkins job url.")
        parser.add_argument(
            '--jenkins-build-number', help="Specify jenkins build number.")

        args = parser.parse_args()
        if args.version:
            print("jenkins-mail-py version: {}".format(__version__))
            return

        self.mailgun_smtp_username = args.mailgun_smtp_username
        self.mailgun_smtp_password = args.mailgun_smtp_password
        self.mail_sender = args.mail_sender
        self.mail_recepients = args.mail_recepients

        self.jenkins_job_name = args.jenkins_job_name
        self.jenkins_job_url = args.jenkins_job_url
        self.jenkins_build_number = args.jenkins_build_number

        if not (self.mailgun_smtp_username and self.mailgun_smtp_password and \
                self.mail_sender and self.mail_recepients):
            print("mailgun configuration error, emails can not be sent.")
            self.config_ready = False
        elif not (self.jenkins_job_name and self.jenkins_job_url and self.jenkins_build_number):
            print("jenkins configuration missed, emails can not be sent.")
            self.config_ready = False
        else:
            self.config_ready = True
            self.mailgun_server_addr = "smtp.mailgun.org"

    def send_mail(self, subject, content="", flag_code=0):
        if not self.config_ready:
            print("configuration error, emails can not be sent.")
            sys.exit(1)
            
        subject = "-".join([self.jenkins_job_name, subject])
        
        try:
            server = smtplib.SMTP("smtp.mailgun.org", 587)
            
            server.login(self.mailgun_smtp_username, self.mailgun_smtp_password)
            
            msg = MIMEText(self.gen_mail_html_content(content, flag_code), _subtype='html', _charset='utf-8')
            msg["Subject"] = subject
            msg["From"] = self.mail_sender
            msg["To"] = ";".join(self.mail_recepients)
            
            server.sendmail(msg["From"], msg["To"], msg.as_string())
            
            server.quit()
            
            print("Email sent")
        except Exception, e:
            print("SMTP Failed!!! \nDetail Information below:")
            print(repr(e))

    def gen_mail_html_content(self, content, flag_code):
        content_bgcolor = "#b3ffe6" if flag_code == 0 else "#FF8A80"
        content_html = """
            <HTML>
                <body bgcolor="{content_bgcolor}">
                    <h2>&nbspJenkins job: {jenkins_job_name}</h2>
                    <p>{content}</p>
                    <p>&nbspView <a href='{jenkins_job_url}/{jenkins_build_number}'>Jenkins job</a>.</p>
                </body>
            </HTML>""".format(
                jenkins_job_name=self.jenkins_job_name,
                content_bgcolor=content_bgcolor,
                content=self.format_content(content),
                jenkins_job_url=self.jenkins_job_url,
                jenkins_build_number=self.jenkins_build_number
            )

        return content_html

    def format_content(self, content, level=1):
        if not isinstance(content, dict):
            return str(content)

        formated_content = "<br/>"

        for key, value in content.items():
            formated_content += "&nbsp&nbsp&nbsp&nbsp" * level
            formated_content += "{}:&nbsp".format(key)
            formated_content += self.format_content(value, level + 1) + "<br/>"

        return formated_content
