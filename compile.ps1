function Write-Info($str) {
    $host.UI.RawUI.ForegroundColor = "Blue"
    Write-Output($str) | Out-Default
    $host.UI.RawUI.ForegroundColor = "White"
}

if (Test-Path .venv){
    Write-Info("Deleting virtual environment") | Out-Default
    Remove-Item -Recurse -Force .venv
    Write-Info("Creating virtual environment") | Out-Default
    python -m venv .venv
    Write-Info("Installing packages") | Out-Default
    .venv\Scripts\python.exe -m pip install -r requirements.txt
}
.venv\Scripts\Activate.ps1
Write-Info("Creating executable")
pyinstaller check.py
Write-output("Copying distributable to readme_check")
if (Test-Path .\readme_check) {Remove-Item -Recurse readme_check}
Copy-Item -Recurse dist\* readme_check\
Write-Info("Removing build artifacts")
Remove-Item -Recurse .\build
Remove-Item -Recurse .\dist
Remove-Item .\check.spec
deactivate
