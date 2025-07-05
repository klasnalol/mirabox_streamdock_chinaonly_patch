# mirabox_streamdock_chinaonly_patch
# Patch for StreamDock – Disable Forced Chinese Locale Popup

## Patch Summary
This patch inverts the conditional branch so the forced Chinese popup is bypassed for non-zh_CN locales.
removes the forced popup that appears when the application is not running under a `zh_CN` (Chinese) locale. It modifies a single byte in the executable to bypass the locale check while preserving full functionality of the device.

### Target Binary
- Architecture: x86_64
- UI framework: Qt5

### Patch Location
- **Address**: `0x14026C7E0`
- **Original**: `75 49` (JNZ)
- **Patched**: `74 49` (JZ)
  
### MANUAL PATCH
### Instructions (Ghidra)
1. Load Streamdock.exe in Ghidra.
2. Go to `0x14026C7E0`.
3. Right-click → `Patch Instruction`.
4. Change `JNZ 0x14026C82B` → `JZ 0x14026C82B`.


## How to Apply using PYTHON PATCH

> Requires [Python](https://www.python.org/downloads/) installed.

1. Download `patch.py`.
2. Place it in the same folder as your original `StreamDock.exe`.
3. Run the following command in PowerShell or CMD:

```bash
python patch.py StreamDock.exe
```

✅ You should see:

```
[✔] Patch applied at 0x26BBE0: 75 → 74
```


## ⚠️ Warnings

WAS TESTED ON 3.10.193.0615 version
* Always **back up your original `.exe`** before patching.
* This patch assumes the binary was not packed or modified.
* If the byte at offset `0x26BBE0` is **not `75`**, do **not apply** the patch — your version may differ.

---

## ✅ After Patching

* The app **no longer shows the forced Chinese popup**.
* The **device works normally**.
* If your locale is `zh_CN`, the popup still appears (intended behavior preserved).

---

## 📜 License

This patch is provided for educational and interoperability purposes. You are responsible for complying with your local laws and software license agreements.

