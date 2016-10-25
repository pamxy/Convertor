
call shared.bat

cmd /k "cd .\%FOLDER_NAME%\Scripts & activate & cd /d .\..\..\install & cd 32\pymupdf-1.9.2.0-py34-x86\fitz & python setup.py install"

rem pause
