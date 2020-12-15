import os
from pathlib import Path
from dotenv import load_dotenv

class DsConfig:
    instance = None
    config = {}

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = DsConfig()
        return cls.instance

    def __init__(self):
        client_id = os.environ.get('DS_CLIENT_ID', None)
        if client_id is None:
            load_dotenv()

        self.config['DS_AUTH_SERVER'] = os.environ.get('REACT_APP_DS_AUTH_SERVER')
        self.config['DS_RETURN_URL'] = os.environ.get('REACT_APP_DS_RETURN_URL')

        self.config['DS_CLIENT_ID'] = os.environ.get('DS_CLIENT_ID', None)
        self.config['DS_CLIENT_SECRET'] = os.environ.get('DS_CLIENT_SECRET')
        self.config['DS_IMPERSONATED_USER_GUID'] = os.environ.get('DS_IMPERSONATED_USER_GUID')
        self.config['DS_TARGET_ACCOUNT_ID'] = os.environ.get('DS_TARGET_ACCOUNT_ID')
        self.config['DS_PRIVATE_KEY'] = os.environ.get('DS_PRIVATE_KEY')
        self.config['DS_PAYMENT_GATEWAY_ID'] = os.environ.get('DS_PAYMENT_GATEWAY_ID')
        self.config['DS_PAYMENT_GATEWAY_NAME'] = os.environ.get('DS_PAYMENT_GATEWAY_NAME')
        self.config['DS_PAYMENT_GATEWAY_DISPLAY_NAME'] = os.environ.get('DS_PAYMENT_GATEWAY_DISPLAY_NAME')
        if not self.config['DS_CLIENT_ID']:
            raise Exception(f'Missing config file |.env| and environment variables are not set.')

    @classmethod
    def auth_server(cls):
        return cls.get_instance().config['DS_AUTH_SERVER']

    @classmethod
    def client_id(cls):
        return cls.get_instance().config['DS_CLIENT_ID']

    @classmethod
    def client_secret(cls):
        return cls.get_instance().config['DS_CLIENT_SECRET']

    @classmethod
    def impersonated_user_guid(cls):
        return cls.get_instance().config['DS_IMPERSONATED_USER_GUID']

    @classmethod
    def target_account_id(cls):
        return cls.get_instance().config['DS_TARGET_ACCOUNT_ID']

    @classmethod
    def private_key(cls):
        d = cls.get_instance().config['DS_PRIVATE_KEY']
        fName = Path.cwd() / d
        if  fName.is_file():
            b = bytes(open(fName,'rb').read())
            return b
        else:
            return d
        
    @classmethod
    def gateway_id(cls):
        return cls.get_instance().config['DS_PAYMENT_GATEWAY_ID']

    @classmethod
    def set_gateway_id(cls, gateway_id):
        cls.get_instance().config['DS_PAYMENT_GATEWAY_ID'] = gateway_id

    @classmethod
    def gateway_name(cls):
        return cls.get_instance().config['DS_PAYMENT_GATEWAY_NAME']

    @classmethod
    def set_gateway_name(cls, gateway_name):
        cls.get_instance().config['DS_PAYMENT_GATEWAY_NAME'] = gateway_name

    @classmethod
    def gateway_display_name(cls):
        return cls.get_instance().config['DS_PAYMENT_GATEWAY_DISPLAY_NAME']

    @classmethod
    def set_gateway_display_name(cls, gateway_display_name):
        cls.get_instance().config['DS_PAYMENT_GATEWAY_DISPLAY_NAME'] = gateway_display_name

    @classmethod
    def return_url(cls):
        return cls.get_instance().config['DS_RETURN_URL']

    @classmethod
    def aud(cls):
        auth_server = cls.auth_server()
        if 'https://' in auth_server:
            aud = auth_server[8:]
        else:
            aud = auth_server[7:]
        return aud

    @classmethod
    def permission_scopes(cls):
        return ['signature', 'impersonation', 'click.manage']

    @classmethod
    def code_grant_scopes(cls):
        return ['signature', 'click.manage']
