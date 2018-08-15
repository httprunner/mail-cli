# Mail CLI

CLI for email sending, based on mailgun service and SMTP mailer.

## Install

```bash
$ pip install -U mailcli
```

## Usage

```text
$ mailcli -h
usage: mailcli [-h] [-V] [-u MAILGUN_SMTP_USERNAME]
                  [-p MAILGUN_SMTP_PASSWORD] [--mail-sender MAIL_SENDER]
                  [--mail-recepients [MAIL_RECEPIENTS [MAIL_RECEPIENTS ...]]]
                  [--mail-subject MAIL_SUBJECT] [--mail-content MAIL_CONTENT]
                  [--mail-content-path MAIL_CONTENT_PATH]

Mail-CLI, send mail with mailgun service.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show version
  -u MAILGUN_SMTP_USERNAME, --mailgun-smtp-username MAILGUN_SMTP_USERNAME
                        Specify mailgun smtp username.
  -p MAILGUN_SMTP_PASSWORD, --mailgun-smtp-password MAILGUN_SMTP_PASSWORD
                        Specify mailgun smtp password.
  --mail-sender MAIL_SENDER
                        Specify email sender.
  --mail-recepients [MAIL_RECEPIENTS [MAIL_RECEPIENTS ...]]
                        Specify email recepients.
  --mail-subject MAIL_SUBJECT
                        Specify email subject.
  --mail-content MAIL_CONTENT
                        Specify email content.
  --mail-content-path MAIL_CONTENT_PATH
                        Load file content as mail content.
```

## Examples

### send mail with content

```bash
$ mailcli \
    -u "user@mail.com" \
    -p "pwd123" \
    --mail-sender "sender@mail.com" \
    --mail-recepients test1@mail.com test2@mail.com \
    --mail-subject subject-test \
    --mail-content hello-world
```

### send mail with file content

```bash
$ mailcli \
    -u "user@mail.com" \
    -p "pwd123" \
    --mail-sender "sender@mail.com" \
    --mail-recepients test1@mail.com test2@mail.com \
    --mail-subject subject-test \
    --mail-content-path 1534006836.html
```
