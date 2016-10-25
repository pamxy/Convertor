
call shared.bat

cmd /k "cd .\%FOLDER_NAME%\Scripts & activate & cd /d .\..\.. & pip3 install -r requirements.txt"

rem pause
