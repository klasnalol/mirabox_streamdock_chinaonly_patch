# mirabox_streamdock_chinaonly_patch
# Ghidra Patch – Disable Forced Chinese Locale Popup

## Patch Summary
This patch inverts the conditional branch so the forced Chinese popup is bypassed for non-zh_CN locales.

### Target Binary
- Architecture: x86_64
- UI framework: Qt5

### Patch Location
- **Address**: `0x14026C7E0`
- **Original**: `75 49` (JNZ)
- **Patched**: `74 49` (JZ)

### Instructions (Ghidra)
1. Load Streamdock.exe in Ghidra.
2. Go to `0x14026C7E0`.
3. Right-click → `Patch Instruction`.
4. Change `JNZ 0x14026C82B` → `JZ 0x14026C82B`.

### Result
- The popup no longer shows unless the locale is zh_CN.
- Device functionality remains intact.
