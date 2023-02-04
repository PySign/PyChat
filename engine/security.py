#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-02-2023 01:14 pm
# @Author  : bhaskar.uprety
# @File    : security

"""security File created on 04-02-2023"""
import base64

import rsa
from rsa import VerificationError
from pyotp import TOTP
from .data import config_data


def generate_keypair():
    """Implemented generate_keypair"""
    public_key, private_key = rsa.newkeys(384)

    # Convert public key to PEM string
    public_key_pem = public_key.save_pkcs1().decode()
    # Convert private key to PEM string
    private_key_pem = private_key.save_pkcs1().decode()

    return public_key_pem, private_key_pem


def encrypt_username(username: str, public_key_pem: str):
    """Implemented encrypt_username"""
    public_key = rsa.PublicKey.load_pkcs1(public_key_pem.encode())
    encrypted_username = rsa.encrypt(username.encode(), public_key)
    return encrypted_username.hex()


def decrypt_username(encrypted_username: str, private_key_pem: str):
    """Implemented decrypt_username"""
    private_key = rsa.PrivateKey.load_pkcs1(private_key_pem.encode())
    decrypted_username = rsa.decrypt(bytes.fromhex(encrypted_username), private_key).decode()
    return decrypted_username


def get_signature(data: str, private_key_pem: str):
    """Implemented get_signature"""
    private_key = rsa.PrivateKey.load_pkcs1(private_key_pem.encode())
    sign = rsa.sign(data.encode(), private_key, 'SHA-1')
    return sign.hex()


def verify_signature(data: str, sign: str, public_key_pem: str):
    """Implemented verify_signature"""
    public_key = rsa.PublicKey.load_pkcs1(public_key_pem.encode())
    try:
        method = rsa.verify(data.encode(), bytes.fromhex(sign), public_key)
        ret = method == 'SHA-1'
    except VerificationError:
        ret = False
    return ret


def get_totp() -> str:
    """Create TOTP"""
    conf = config_data()
    totp_code = conf['totp_code']
    totp_code_b32 = base64.b32encode(totp_code.encode()).decode()
    totp = TOTP(totp_code_b32)
    return totp.now()
