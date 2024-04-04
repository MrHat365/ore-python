"""
  @ Author:   Mr.Hat
  @ Date:     2024/4/4 18:47
  @ Description: 
  @ History:
"""
from __future__ import annotations

import base58


class PublicKey:
    LENGTH = 32

    def __init__(self, value: bytearray | bytes | int | str | list[int]):
        if isinstance(value, str):
            try:
                self.byte_value = base58.b58decode(value)
            except ValueError:
                raise ValueError("Invalid public key.")

        elif isinstance(value, int):
            self.byte_value = bytes([value])

        else:
            self.byte_value = bytes(value)

        if len(self.byte_value) != self.LENGTH:
            raise ValueError("Invalid public key, the length is wrong.")

    def __bytes__(self) -> bytes:
        return (
            self.byte_value
            if len(self.byte_value) == self.LENGTH
            else self.byte_value.rjust(self.LENGTH, b"\0")
        )

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.base58_encode().decode("utf-8")

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, PublicKey):
            return self.byte_value == __value.byte_value
        return False

    def base58_encode(self) -> bytes:
        return base58.b58encode(bytes(self))

    def base58_decode(self) -> bytes:
        return base58.b58decode(self.byte_value)