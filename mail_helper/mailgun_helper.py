import argparse
import sys
import requests


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
            '--email-sender', help="Specify email sender.")
        parser.add_argument(
            '--email-recepients', help="Specify email recepients.")

        args = parser.parse_args()
        mailgun_api_id = args.mailgun_api_id
        self.mailgun_api_key = args.mailgun_api_key
        self.email_sender = args.email_sender
        self.email_recepients = args.email_recepients

        if not (mailgun_api_id and self.mailgun_api_key and \
                self.email_sender and self.email_recepients):
            print("mailgun configuration error, emails can not be sent.")
            self.config_ready = False
        else:
            self.config_ready = True
            self.mailgun_api_url = "https://api.mailgun.net/v3/{}/messages".format(mailgun_api_id)

    def send_mail(self, subject, text=None, html=None):
        if not self.config_ready:
            print("mailgun configuration error, emails can not be sent.")
            sys.exit(1)

        data={
            "subject": subject,
            "from": "postmaster <{}>".format(self.email_sender),
            "to": self.email_recepients,
            "text": text,
            "html": html
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
