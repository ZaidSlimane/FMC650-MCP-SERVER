#!/usr/bin/env python3
"""Decrypt a Teltonika .xim firmware container (proven on FMX65 03.01.01.Rev.15).

Container (little-endian), derived from Teltonika.Firmware.Reader IL:

  magic       4   "TLTF"
  version     u32
  reserved    8
  saltLen     u32 (0x20)
  salt        saltLen
  ivLen       u32 (0x10)
  iv          ivLen
  payloadLen  u32
  payload     payloadLen          AES-256-CBC ciphertext -> gzip stream
  tail        u32 0x80 + 128-byte RSA-2048 signature

Key = PBKDF2-HMAC-SHA1(password = base64decode(PASSWORD_B64), salt, 1000, 32)

The password below is an embedded constant recovered from the vendor reader's
obfuscated string blob (b[i] ^= (i & 0xFF) ^ 0xAA). It is not a user secret.

Usage: xim_decrypt.py <file.xim> <out.bin>
"""
import base64
import gzip
import hashlib
import struct
import sys

PASSWORD_B64 = "hX9Xe0ttKg0SOCPRbAjdAcPy6VD96NRYo9GQ00MrEfU="


def decrypt(data):
    if data[:4] != b"TLTF":
        raise ValueError("not a TLTF container")
    off = 4
    version = struct.unpack_from("<I", data, off)[0]; off += 4
    off += 8
    salt_len = struct.unpack_from("<I", data, off)[0]; off += 4
    salt = data[off:off + salt_len]; off += salt_len
    iv_len = struct.unpack_from("<I", data, off)[0]; off += 4
    iv = data[off:off + iv_len]; off += iv_len
    payload_len = struct.unpack_from("<I", data, off)[0]; off += 4
    payload = data[off:off + payload_len]
    tail = data[off + payload_len:]

    key = hashlib.pbkdf2_hmac("sha1", base64.b64decode(PASSWORD_B64), salt, 1000, 32)

    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    plain = dec.update(payload) + dec.finalize()

    # single gzip member; the plaintext carries trailing padding that
    # gzip.decompress() would treat as a second member header
    import zlib
    do = zlib.decompressobj(16 + zlib.MAX_WBITS)
    image = do.decompress(plain) + do.flush()
    meta = {
        "unused_padding": len(do.unused_data),
        "version": version,
        "salt_len": salt_len,
        "iv_len": iv_len,
        "payload_len": payload_len,
        "tail_len": len(tail),
        "image_len": len(image),
        "image_sha256": hashlib.sha256(image).hexdigest(),
        "plain_is_gzip": plain[:2] == b"\x1f\x8b",
    }
    return image, meta


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    image, meta = decrypt(open(src, "rb").read())
    open(dst, "wb").write(image)
    for k, v in meta.items():
        print(f"{k}: {v}")
