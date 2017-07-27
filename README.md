# mail helper

Encapsulation for email senders, include mailgun service and SMTP mailer.

## Install

To install mail helper, run this command in your terminal:

```bash
$ pip install -U git+https://github.com/debugtalk/mail-hepler.git#egg=mail-helper
```

## Usage

In your `CLI` entrance script, you can use mail helper like below.

```python
from mail_helper import MailgunHelper

def main():
    """ parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(
        description='CLI application example.')

    parser.add_argument(
        '--log-level', default='INFO',
        help="Specify logging level, default is INFO.")
    parser.add_argument(
        '--host', help="Specify test host.")

    mailer = MailgunHelper(parser)
    args = parser.parse_args()

def start(args, mailer=None):

    # do your work

    # send result via email
    if mailer and mailer.config_ready:
        subject = "this is title"
        html_content = "<html><p>this is html content</p></html>"
        mailer.send_mail(subject, html=html_content)
```

And then, you can use mail helper in command shell.

```text
$ python main.py -h

usage: main.py [-h] [--log-level LOG_LEVEL] [--host HOST]
               [--mailgun-api-id MAILGUN_API_ID]
               [--mailgun-api-key MAILGUN_API_KEY]
               [--email-sender EMAIL_SENDER]
               [--email-recepients EMAIL_RECEPIENTS]

CLI application example.

optional arguments:
  -h, --help            show this help message and exit
  --log-level LOG_LEVEL
                        Specify logging level, default is INFO.
  --host HOST
                        Specify test host.
  --mailgun-api-id MAILGUN_API_ID
                        Specify mailgun api id.
  --mailgun-api-key MAILGUN_API_KEY
                        Specify mailgun api key.
  --email-sender EMAIL_SENDER
                        Specify email sender.
  --email-recepients EMAIL_RECEPIENTS
                        Specify email recepients.
```

## Example

```bash
$ python main.py --seeds http://debugtalk.com --crawl-mode bfs --max-depth 1 --mailgun-api-id samples.mailgun.org --mailgun-api-key key-3ax6xnjp29jd6fds4gc373sgvjxteol0 --email-sender excited@samples.mailgun.org --email-recepients test@email.com
```
