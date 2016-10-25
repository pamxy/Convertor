call .\..\..\shared.bat
rem #############################


cmd /k "cd .\..\..\%FOLDER_NAME%\Scripts & activate & cd /d .\..\src & python generate_qry.py"


pause
