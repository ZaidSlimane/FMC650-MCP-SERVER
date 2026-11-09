---
title: FMX65 / FMC650 .xim firmware decryption
device: FMX65 (= FMC650)
firmware: Ver.03.01.01.Rev.15
configurator: 1.8.26_B.FMX6_R.194
status: verified
verified: 2026-11-05
---

# `.xim` decryption — verified

Reproduced end to end with [`../tools/xim_decrypt.py`](../tools/xim_decrypt.py):

```
image_len:      1050472
image_sha256:   e20fafd9aeefe5860083b047c1f291a1d992eda65610bdab46712e1a4f239195
unused_padding: 15
```

The sha256 matches the previously decrypted `fw_image.bin` byte for byte.

## Container layout

Little-endian, from `Teltonika.Firmware.Reader` CIL:

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 4 | magic `TLTF` |
| 4 | 4 | version (1 for this build) |
| 8 | 8 | reserved (zero) |
| 16 | 4 | `saltLen` = 0x20 |
| 20 | 32 | salt |
| 52 | 4 | `ivLen` = 0x10 |
| 56 | 16 | IV |
| 72 | 4 | `payloadLen` = 1,037,776 |
| 76 | `payloadLen` | AES-256-CBC ciphertext |
| 76+payloadLen | 4 | 0x80 (signature length) |
| … | 128 | detached RSA-2048 signature |

File size 1,037,984 = 76 + 1,037,776 + 4 + 128. There is **no** per-frame
partition table at this layer: the decrypted payload is a single gzip member.

## Key derivation

```
password = base64decode("hX9Xe0ttKg0SOCPRbAjdAcPy6VD96NRYo9GQ00MrEfU=")   # raw 32 bytes
key      = PBKDF2-HMAC-SHA1(password, salt, 1000, dkLen=32)
plain    = AES-256-CBC-decrypt(key, iv, payload)
image    = inflate(plain)          # single member, 15 bytes trailing padding
```

The base64 **string decoded to bytes** is the password; using the ASCII string
instead yields non-gzip plaintext (checked: head `06 57 12 a2`).

## Where the constant comes from

The reader assembly is obfuscated (Hangul identifiers). Its string blob is
decoded with `b[i] ^= (i & 0xFF) ^ 0xAA` over 0x56E bytes; the decoded blob
contains the base64 password, an RSA-2048 public key and a private key XML used
by the legacy (non-zero-version) container path. The password is a vendor
constant, not a user secret.

## Legacy path (other firmware generations)

Older containers (non-zero version) carry key/IV blobs in per-frame headers and
unwrap them with the recovered RSA private key, then the same PBKDF2→AES step.
Only the version-1 path above is exercised by these three `.xim` files.

## Not done here

The decrypted image (`fw_image.bin`, 1,050,472 B) is **not** partition-parsed.
It is not itself a gzip; it starts with zeros then a table of little-endian ints
(`01 00 00 00 10 00 00 00 03 00 00 00 …`). Extracting a parameter descriptor
table from it is still open — see `analysis_report.md`.
