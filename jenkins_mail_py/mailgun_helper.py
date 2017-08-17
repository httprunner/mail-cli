import argparse
import sys
import requests
from . import __version__


class MailgunHelper(object):

    def __init__(self, parser=None):
        """
        config = {
            'api-id': 'samples.mailgun.org',
            'api-key': 'key-3ax6xnjp29jd6fds4gc373sgvjxteol0',
            'sender': 'excited@samples.mailgun.org'
        }
        """
        parser = parser or argparse.ArgumentParser(
            description='Mailgun helper, send mail with mailgun service.')

        parser.add_argument(
            '--mailgun-api-id', help="Specify mailgun api id.")
        parser.add_argument(
            '--mailgun-api-key', help="Specify mailgun api key.")
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

        mailgun_api_id = args.mailgun_api_id
        self.mailgun_api_key = args.mailgun_api_key
        self.mail_sender = args.mail_sender
        self.mail_recepients = args.mail_recepients

        self.jenkins_job_name = args.jenkins_job_name
        self.jenkins_job_url = args.jenkins_job_url
        self.jenkins_build_number = args.jenkins_build_number

        if not (mailgun_api_id and self.mailgun_api_key and \
                self.mail_sender and self.mail_recepients):
            print("mailgun configuration error, emails can not be sent.")
            self.config_ready = False
        elif not (self.jenkins_job_name and self.jenkins_job_url and self.jenkins_build_number):
            print("jenkins configuration missed, emails can not be sent.")
            self.config_ready = False
        else:
            self.config_ready = True
            self.mailgun_api_url = "https://api.mailgun.net/v3/{}/messages".format(mailgun_api_id)

    def send_mail(self, subject, content="", flag_code=0):
        if not self.config_ready:
            print("configuration error, emails can not be sent.")
            sys.exit(1)

        subject = "-".join([self.jenkins_job_name, subject])
        content_html = self.gen_mail_html_content(content, flag_code)
        data = {
            "subject": subject,
            "from": "postmaster <{}>".format(self.mail_sender),
            "to": ",".join(self.mail_recepients),
            "html": content_html
        }
        resp = requests.post(
            self.mailgun_api_url,
            auth=("api", self.mailgun_api_key),
            data=data
        )
        try:
            assert "Queued. Thank you." in resp.json()['message']
            print(resp.text)
        except:
            print(resp.text)

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
