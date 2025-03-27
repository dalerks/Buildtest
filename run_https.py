import os
from django.core.management import execute_from_command_line
from django.core.management.commands.runserver import Command as RunserverCommand
import ssl

class Command(RunserverCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--cert-file', default='localhost.crt', help='SSL certificate file')
        parser.add_argument('--key-file', default='localhost.key', help='SSL key file')

    def handle(self, *args, **options):
        cert_file = options['cert_file']
        key_file = options['key_file']
        self.use_ssl = True
        self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        return super().handle(*args, **options)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Buildtest.settings")
    execute_from_command_line(["manage.py", "runserver", "5001"])
