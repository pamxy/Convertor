call .\..\..\shared.bat
rem #############################

rem call pyuic4 UIMainWindow.ui -o UIMainWindow.py

cmd /k "cd .\..\..\%FOLDER_NAME%\Scripts & activate & cd /d .\..\src & call pyuic4 UIMainWindow.ui -o UIMainWindow.py"

rem pause

pause
