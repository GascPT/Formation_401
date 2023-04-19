# Control 1.1.5 (L1)
# Ensure 'Password must meet complexity requirements' is set to 'Enabled'

secedit /export /cfg C:\secpol\securityconfig.cfg

((get-content C:\secpol\securityconfig.cfg) -replace ('PasswordComplexity = 0', 'PasswordComplexity = 1')) | Out-File C:\secpol\securityconfig.cfg #carriage return
secedit /configure /db $env:windir\security\new.sdb /cfg C:\secpol\securityconfig.cfg /areas SECURITYPOLICY #carriage return
