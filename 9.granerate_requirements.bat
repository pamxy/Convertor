
call shared.bat

cmd /k "cd .\%FOLDER_NAME%\Scripts & activate & cd /d .\..& pip3 freeze > ../requirements_src.txt"

rem pause
