# Control 18.3.2 (L1)
# Ensure 'Configure SMB v1 server' is set to 'Disabled'

# Set the value for SMB v1 server configuration
$SMBv1ServerConfig = 0

# Set the registry path for SMB v1 server configuration
$RegistryPath = "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"

# Check if the SMB v1 server configuration is already set to the desired value
$CurrentValue = Get-ItemPropertyValue -Path $RegistryPath -Name "SMB1" -ErrorAction SilentlyContinue
if ($CurrentValue -eq $SMBv1ServerConfig) {
    Write-Host "The SMB v1 server configuration is already set to $SMBv1ServerConfig."
} else {
    # Set the SMB v1 server configuration to the desired value
    Set-ItemProperty -Path $RegistryPath -Name "SMB1" -Value $SMBv1ServerConfig -Type DWord -Force
    Write-Host "The SMB v1 server configuration has been set to $SMBv1ServerConfig."
}
