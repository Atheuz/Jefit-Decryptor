"""Jefit Decryptor."""
import os

from Crypto.Cipher import DES


class JefitDecryptor:
    """JefitDecryptor class. Decrypt data from Jefit mobile app database."""

    def __init__(self, filepath):
        """JefitDecryptor constructor."""
        self.filepath = filepath
        self.filepath_no_ext, self.ext = os.path.splitext(self.filepath)
        self.file_base_name = os.path.basename(self.filepath_no_ext)
        self.decrypted_filepath = "output/{}_decrypted.db".format(self.file_base_name)

    def decrypt(self):
        """Get the Jefit data from the encrypted database file."""
        key = b"HignDlPs"
        enc = open(self.filepath, "rb").read()
        des = DES.new(key, DES.MODE_ECB)
        output = des.decrypt(enc)
        with open(self.decrypted_filepath, "wb") as file:
            file.write(output)
