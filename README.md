# Jenkins mail helper

Encapsulation for email senders, include mailgun service and SMTP mailer.

## Install

To install mail helper, run this command in your terminal:

```bash
$ pip install -U git+https://github.com/debugtalk/jenkins-mail-py.git#egg=jenkins-mail-py
```

## Usage

In your `CLI` entrance script, you can use mail helper like below.

```python
import argparse
from jenkins_mail_py import MailgunHelper

def main():
    """ parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(
        description='CLI application example.')

    parser.add_argument(
        '--log-level', default='INFO',
        help="Specify logging level, default is INFO.")

    mailer = MailgunHelper(parser)
    args = parser.parse_args()

    start(args, mailer)

def start(args, mailer=None):

    # do your work

    # send result via email
    if mailer and mailer.config_ready:
        subject = "FAIL"
        content = {
            'testset1.yml': {'total': 16, 'successes': 16, 'failures': 0, 'errors': 0, 'skipped': 0},
            'testset2.yml': {'total': 18, 'successes': 16, 'failures': 2, 'errors': 0, 'skipped': 0},
        }
        flag_code = 1
        mailer.send_mail(subject, content, flag_code)

if __name__ == '__main__':
    main()
```

And then, you can use mail helper in command shell.

```text
$ python demo_mailgun.py -h
usage: demo_mailgun.py [-h] [--log-level LOG_LEVEL]
                       [--mailgun-api-id MAILGUN_API_ID]
                       [--mailgun-api-key MAILGUN_API_KEY]
                       [--email-sender EMAIL_SENDER]
                       [--email-recepients [EMAIL_RECEPIENTS [EMAIL_RECEPIENTS ...]]]
                       [--mail-subject MAIL_SUBJECT]
                       [--mail-content MAIL_CONTENT]
                       [--jenkins-job-name JENKINS_JOB_NAME]
                       [--jenkins-job-url JENKINS_JOB_URL]
                       [--jenkins-build-number JENKINS_BUILD_NUMBER]

CLI application example.

optional arguments:
  -h, --help            show this help message and exit
  --log-level LOG_LEVEL
                        Specify logging level, default is INFO.
  --mailgun-api-id MAILGUN_API_ID
                        Specify mailgun api id.
  --mailgun-api-key MAILGUN_API_KEY
                        Specify mailgun api key.
  --email-sender EMAIL_SENDER
                        Specify email sender.
  --email-recepients [EMAIL_RECEPIENTS [EMAIL_RECEPIENTS ...]]
                        Specify email recepients.
  --mail-subject MAIL_SUBJECT
                        Specify email subject.
  --mail-content MAIL_CONTENT
                        Specify email content.
  --jenkins-job-name JENKINS_JOB_NAME
                        Specify jenkins job name.
  --jenkins-job-url JENKINS_JOB_URL
                        Specify jenkins job url.
  --jenkins-build-number JENKINS_BUILD_NUMBER
                        Specify jenkins build number.
```

## Example

```bash
$ python main.py --seeds http://debugtalk.com --crawl-mode bfs --max-depth 1 --mailgun-api-id samples.mailgun.org --mailgun-api-key key-3ax6xnjp29jd6fds4gc373sgvjxteol0 --email-sender excited@samples.mailgun.org --email-recepients test@email.com --jenkins-job-name demo-smoketest --jenkins-job-url http://test.debugtalk.com/job/demo-smoketest/ --jenkins-build-number 69
```
