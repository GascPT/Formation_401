# Control 1.1.5 (L1)
# Ensure 'Password must meet complexity requirements' is set to 'Enabled'

# Set the value for 'Password must meet complexity requirements' configuration
$PasswordComplexityConfig = "Enabled"

# Set the local security policy path for 'Password must meet complexity requirements' configuration
$PolicyPath = "SeSecurityPrivilege"

# Check if 'Password must meet complexity requirements' is already set to the desired value
$CurrentValue = Get-ItemPropertyValue -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "PasswordComplexity" -ErrorAction SilentlyContinue
if ($CurrentValue -eq $PasswordComplexityConfig) {
    Write-Host "'Password must meet complexity requirements' is already set to $PasswordComplexityConfig."
} else {
    # Set 'Password must meet complexity requirements' to the desired value
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "PasswordComplexity" -Value $PasswordComplexityConfig -Type DWord -Force
    Write-Host "'Password must meet complexity requirements' has been set to $PasswordComplexityConfig."
}
