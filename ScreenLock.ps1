# Enable automatic screen lock
# Define the timeout value (in seconds)
$timeout = 900

# Enable screen saver and set timeout
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveActive /t REG_SZ /d 1 /f
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveTimeOut /t REG_SZ /d $timeout /f

# Configure screen saver to require password on resume
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /d 1 /f
reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Control Panel\Desktop" /v ScreenSaverGracePeriod /t REG_SZ /d 0 /f
reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Control Panel\Desktop" /v ScreenSaverLockTimeout /t REG_SZ /d $timeout /f

# Enable the screen saver
Start-Process -FilePath "C:\WINDOWS\system32\scrnsave.scr" -ArgumentList "/s"
