"""System Bridge: Windows Autostart"""
import os
import platform
import sys


def autostart_windows_disable():
    """Disable autostart for Windows"""
    if platform.system() != "Windows":
        return

    # pylint: disable=import-error, import-outside-toplevel
    from winreg import HKEY_CURRENT_USER, KEY_ALL_ACCESS, CloseKey, DeleteValue, OpenKey

    try:
        key = OpenKey(
            HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            reserved=0,
            access=KEY_ALL_ACCESS,
        )
        if key is None:
            return
        DeleteValue(key, "systembridge")
        CloseKey(key)
    except OSError:
        pass


def autostart_windows_enable():
    """Enable autostart for Windows"""
    if platform.system() != "Windows":
        return

    # pylint: disable=import-error, import-outside-toplevel
    from winreg import (
        HKEY_CURRENT_USER,
        KEY_ALL_ACCESS,
        REG_SZ,
        CloseKey,
        OpenKey,
        SetValueEx,
    )

    key = OpenKey(
        HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        reserved=0,
        access=KEY_ALL_ACCESS,
    )
    SetValueEx(
        key,
        "systembridge",
        0,
        REG_SZ,
        f'"{os.path.join(os.path.dirname(sys.executable), "pythonw.exe")}" -m systembridgebackend'
        if "python" in sys.executable
        else f'"{sys.executable}"',
    )
    CloseKey(key)
