if (-not(Test-Path .venv)){
    Write-Output("Creating virtual environment")
    python -m venv .venv
    Write-Output("Installing packages")
    .venv\Scripts\python.exe -m pip install -r requirements.txt
}
.venv\Scripts\Activate.ps1
Write-Output("Creating executable")
pyinstaller check.py
Write-output("Copying distributable to readme_check")
if (Test-Path .\readme_check) {Remove-Item -Recurse readme_check}
Copy-Item -Recurse dist\* readme_check\
Write-Output("Removing build artifacts")
Remove-Item -Recurse .\build
Remove-Item -Recurse .\dist
Remove-Item .\check.spec
deactivate
