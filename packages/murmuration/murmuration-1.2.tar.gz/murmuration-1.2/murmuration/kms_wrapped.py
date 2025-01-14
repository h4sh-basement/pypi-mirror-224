import binascii

from boto3 import Session
from botocore.exceptions import ClientError
from .helpers import as_bytes
from .helpers import from_b64_str
from .aws import kms_client
from .helpers import prefix_alias
from .gcm import encrypt_bytes as gcm_encrypt
from .gcm import decrypt_bytes as gcm_decrypt


def encrypt_bytes(
        plain_text: bytes,
        alias: str,
        region: str = None,
        profile: str = None,
        session: Session = None,
        client=None) -> str:
    client = kms_client(region, profile, session, client)
    alias = prefix_alias(alias)
    response = client.generate_data_key(KeyId=alias, KeySpec='AES_256')
    data_key = response['Plaintext']
    header = response['CiphertextBlob']
    value = gcm_encrypt(plain_text, data_key, auth_header=header)
    return value


def decrypt_bytes(
        packed_value: str,
        region: str = None,
        profile: str = None,
        session: Session = None,
        client=None) -> bytes:
    pieces = packed_value.split('|', 1)
    if len(pieces) != 2:
        raise ValueError('Invalid wrapped secret, no data key found')
    wrapped_data_key = pieces[0]
    try:
        wrapped_data_key = from_b64_str(wrapped_data_key)
    except binascii.Error as ex:
        raise ValueError('data key is not properly base64 encoded') from ex
    client = kms_client(region, profile, session, client)
    try:
        response = client.decrypt(CiphertextBlob=wrapped_data_key)
    except ClientError as ex:
        raise ValueError(*ex.args) from ex
    data_key = response['Plaintext']
    plain_text = gcm_decrypt(packed_value, data_key)
    return plain_text


def encrypt(
        plain_text,
        alias,
        region: str = None,
        profile: str = None,
        session: Session = None,
        client=None) -> str:
    plain_text = as_bytes(plain_text)
    data = encrypt_bytes(plain_text, alias, region, profile, session, client)
    return data


def decrypt(
        packed_value: str,
        region: str = None,
        profile: str = None,
        session: Session = None,
        client=None):
    data = decrypt_bytes(packed_value, region, profile, session, client)
    return data.decode('utf-8')
