
call shared.bat
@echo off


rem echo %projectPath%

rem set "PATH=F:\workSpace\Test\python\python34\reportLabTest\RMLViewer\RMLViewer\Lib\site-packages\PyQt4;F:\workSpace\Test\python\python34\reportLabTest\RMLViewer\RMLViewer\Lib\site-packages;F:\workSpace\Test\python\python34\reportLabTest\RMLViewer\RMLViewer\Scripts;%PATH%"
rem @echo on


rem cmd /k "..\Scripts\activate & cd /d .\..\src & python ..\Scripts\nuitka --mingw --recurse-all --show-modules --windows-disable-console --output-dir=.\bin RMLViewer.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & python %ScriptsDir%nuitka --mingw --recurse-all --show-modules --windows-disable-console --output-dir=.\bin calculate.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & python %ScriptsDir%nuitka --recurse-all --show-modules --windows-disable-console --output-dir=.\bin calculate.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & %ScriptsDir%python %ScriptsDir%nuitka --recurse-directory=%mingw64Dir% --output-dir=.\bin calculate.py"
rem nuitka --python-version=3.4 --show-memory --exe --execute --recurse-directory=.\ --mingw --recurse-all --show-progress --show-modules --output-dir=.\bin SecretServer.py


rem cmd /k "%ScriptsDir%activate & cd %srcDir% & python %ScriptsDir%nuitka nuitka  --mingw calculate.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --recurse-all --show-modules --execute --recurse-directory=F:/workSpace/Test/python/python34/NuitkaTest/virtualenvTest/virtualenvTest/libs/python34.lib --recurse-stdlib --show-progress --standalone --mingw calculate.py"
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --recurse-all --execute --recurse-stdlib --standalone --mingw calculate.py"
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & python nuitka calculate.py"
rem set PATH=F:\workSpace\Test\python\python34\NuitkaTest\virtualenvTest\virtualenvTest\src\calculate.build\libs;%PATH%
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --msvc=MSVC calculate.py"
rem echo %PATH%
rem echo %LD_LIBRARY_PATH%
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka calculate.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --mingw --recurse-all --windows-disable-console --standalone --recurse-stdlib --recurse-directory=%site-packagesDir% --output-dir=.\bin RMLViewer.py"
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --msvc=9.0 --standalone --recurse-directory=C:\WorkSpace\RMLViewer\RMLViewer\Lib\site-packages\PyQt4 --execute --recurse-all --output-dir=%curDir%\bin RMLViewer.py"


set vcvarsallDir=C:\WorkTool\Microsoft Visual Studio 9.0\VC
call "%vcvarsallDir%\vcvarsall.bat"
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --msvc=9.0 --standalone --plugin-enable=qt-plugins --windows-disable-console --execute --recurse-all --output-dir=%curDir%\bin RMLViewer.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --msvc=9.0 --debugger --standalone --plugin-enable=qt-plugins --module=C:\WorkSpace\RMLViewer\RMLViewer\Lib\site-packages\fitz;C:\WorkSpace\RMLViewer\RMLViewer\Lib\site-packages\reportlab --windows-disable-console --execute --recurse-all --output-dir=%curDir%\bin RMLViewer_1.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & nuitka --msvc=9.0 --debugger --standalone --plugin-enable=qt-plugins --execute --recurse-all --output-dir=%curDir%\bin MainWindow.py"
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & %ScriptsDir%nuitka --msvc=9.0 --standalone --show-progress --windows-disable-console --plugin-enable=qt-plugins --execute --recurse-all --output-dir=%curDir%\bin MainWindow.py"


rem cmd /k "%ScriptsDir%activate & cd %srcDir% & %ScriptsDir%nuitka --msvc=9.0 --show-modules --standalone --execute --recurse-all --recurse-on --python-version=3.4 --output-dir=%curDir%\bin MainWindow.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & %ScriptsDir%nuitka --msvc=9.0 --debugger --show-modules --recurse-all --recurse-on --python-version=3.4 --output-dir=%curDir%\bin MainWindow.py"
rem cmd /k "%ScriptsDir%activate & cd %srcDir% & %ScriptsDir%nuitka --msvc=9.0 --portable --plugin-enable=qt-plugins --execute --show-modules --recurse-all --recurse-on --python-version=3.4 --output-dir=%curDir%\bin main.py"

rem cmd /k "%ScriptsDir%activate & cd %srcDir% & %ScriptsDir%nuitka --msvc=9.0 --debugger --standalone --plugin-enable=qt-plugins --execute --show-modules --recurse-all --recurse-on --python-version=3.4 --output-dir=%curDir%\bin MainWindow.py"



cmd /k "%ScriptsDir%activate & cd %srcDir% & %ScriptsDir%nuitka --msvc=9.0 --standalone --plugin-enable=qt-plugins --execute --windows-disable-console --show-modules --recurse-all --recurse-on --python-version=3.4 --windows-icon=%srcDir%Convertor.ico --output-dir=%curDir%\bin Convertor.py.py"


pause