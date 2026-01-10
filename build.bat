@echo off
echo Building Quasar Tool...
echo.

pyinstaller --onefile --console ^
--hidden-import=pyisemail ^
--hidden-import=pyisemail.diagnosis ^
--hidden-import=pyisemail.validators ^
--hidden-import=pystyle ^
--hidden-import=termcolor ^
--hidden-import=tqdm ^
--hidden-import=rich ^
--hidden-import=rich.console ^
--hidden-import=rich.text ^
--hidden-import=rich.style ^
--hidden-import=rich.highlighter ^
--hidden-import=rich.pretty ^
--hidden-import=rich.traceback ^
--hidden-import=requests ^
--hidden-import=queue ^
--hidden-import=webbrowser ^
--hidden-import=glob ^
--hidden-import=re ^
--hidden-import=socket ^
--hidden-import=threading ^
--hidden-import=json ^
--hidden-import=time ^
--hidden-import=os ^
--hidden-import=sys ^
--hidden-import=string ^
--hidden-import=subprocess ^
--hidden-import=random ^
--hidden-import=ctypes ^
--hidden-import=ctypes.wintypes ^
--icon=C:\Users\user\Pictures\quASA\icon.ico ^
--name=QuasarTool ^
main_quasar.py

echo.
echo Build complete! Check dist/ folder.
pause
