from typing import (
    Dict
)
from collections.abc import Callable
from aiobotocore.session import get_session
from navconfig import config
from navconfig.logging import logging
from settings.settings import (
    aws_region,
    aws_bucket,
    AWS_CREDENTIALS
)


logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)


class Boto3Client:
    """
    Boto3 AWS Client.

        Overview

        Abstract class for interaction with Boto3 (AWS).

        .. table:: Properties
        :widths: auto

    +------------------------+----------+-----------+-------------------------------------------------------+
    | Name                   | Required | Summary                                                           |
    +------------------------+----------+-----------+-------------------------------------------------------+
    |_credentials            |   Yes    | The function is loaded and then we define the necessary code to   |
    |                        |          | call the script                                                   |
    +------------------------+----------+-----------+-------------------------------------------------------+
    |  _init_                |   Yes    | Component for Data Integrator                                     |
    +------------------------+----------+-----------+-------------------------------------------------------+
    |  _host                 |   Yes    | The IPv4 or domain name of the server                             |
    +------------------------+----------+-----------+-------------------------------------------------------+
    |  get_client            |   Yes    | Gets the client access credentials, by which the user logs in to  |
    |                        |          | perform an action                                                 |
    +------------------------+----------+-----------+-------------------------------------------------------+
    |  print                 |   Yes    | Print message to display                                          |
    +------------------------+----------+-----------+-------------------------------------------------------+
    | get_env_value          |   Yes    | Get env value  policies for setting virtual environment           |
    +------------------------+----------+-----------+-------------------------------------------------------+
    | processing_credentials |   Yes    | client credentials configured for used of the app                 |
    +------------------------+----------+-----------+-------------------------------------------------------+




            Return the list of arbitrary days


    """
    _credentials: Dict = {
        "aws_key": str,
        "aws_secret": str,
        "client_id": str,
        "client_secret": str,
        "service": str,
        "region_name": str,
        "bucket": str
    }

    def __init__(
            self,
            credentials: Dict,
            *args,
            **kwargs
    ) -> None:
        self.region_name: str = None
        self.service: str = None
        self.bucket: str = None
        self.credentials: Dict = credentials
        self._environment: Callable = config

    def define_host(self):
        return True

    def get_client(
            self,
            use_credentials: bool,
            credentials: Dict,
            service: str = 's3'
        ) -> Callable:
        aws_client = None
        if use_credentials is False:
            print("Boto3: Enter anonymous")
            session = get_session()
            aws_client = session.create_client(
                service,
                region_name=credentials['region_name']
            )
        else:
            print("Boto3: Enter signed")
            cred = {
                "aws_access_key_id": credentials['aws_key'],
                "aws_secret_access_key": credentials['aws_secret'],
                "region_name": credentials['region_name'],
            }
            session = get_session()
            aws_client = session.create_client(
                service,
                **cred
            )
        return aws_client

    def get_env_value(self, key, default: str = None):
        if val := self._environment.get(key, default):
            return val
        else:
            return key

    def processing_credentials(self):
        # getting credentials from self.credentials:
        if self.credentials:
            for value, dtype in self._credentials.items():
                try:
                    if value in self.credentials:
                        if type(self.credentials[value]) == dtype:
                            # can process the credentials, extracted from environment or variables:
                            default = getattr(self, value, self.credentials[value])
                            val = self.get_env_value(self.credentials[value], default=default)
                            self.credentials[value] = val
                except (TypeError, KeyError) as err:
                    logging.error(
                    f'{__name__}: Wrong or missing Credentials'
                    )
                    raise Exception(
                        f'{__name__}: Wrong or missing Credentials'
                    ) from err
        else:
            # getting credentials from config
            try:
                aws = AWS_CREDENTIALS[self.config]
            except (KeyError, AttributeError):
                aws = AWS_CREDENTIALS['default']
            self.credentials = aws
        ## getting Tenant and Site from credentials:
        try:
            self.region_name = self.credentials['region_name']
        except KeyError:
            self.region_name = aws_region
        try:
            self.bucket = self.credentials['bucket_name']
        except KeyError:
            self.bucket = aws_bucket
        try:
            self.service = self.credentials['service']
        except KeyError:
            self.service = 's3'
