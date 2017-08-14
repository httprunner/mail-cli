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
        result_flag = "FAIL"
        content = {"total": 10, "success": 8, "fail": 2}
        mailer.send_mail(result_flag, content=content)


if __name__ == '__main__':
    main()
