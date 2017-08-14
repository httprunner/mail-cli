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
