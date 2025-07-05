import sys
import os

# === Patch Details ===
PATCH_OFFSET = 0x26BBE0
ORIGINAL_BYTE = b'\x75'  # JNZ
PATCHED_BYTE  = b'\x74'  # JZ

def patch_file(filepath):
    if not os.path.isfile(filepath):
        print(f"[!] ERROR: File not found: {filepath}")
        return

    with open(filepath, 'rb+') as f:
        f.seek(PATCH_OFFSET)
        current = f.read(1)

        if current != ORIGINAL_BYTE:
            print(f"[!] ERROR: Unexpected byte at 0x{PATCH_OFFSET:X}")
            print(f"    Expected: {ORIGINAL_BYTE.hex()} | Found: {current.hex()}")
            return

        f.seek(PATCH_OFFSET)
        f.write(PATCHED_BYTE)
        print(f"[✔] Patch applied at 0x{PATCH_OFFSET:X}: {ORIGINAL_BYTE.hex()} → {PATCHED_BYTE.hex()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python patch_streamdock.py <path_to_exe>")
        sys.exit(1)

    patch_file(sys.argv[1])
