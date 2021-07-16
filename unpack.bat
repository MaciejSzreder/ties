@echo off
setlocal EnableDelayedExpansion
::get path of folder with project
set repo=%~dp0
::get this bat adress
set clean.bat=%~nx0
set fullpath_clean.bat=%~f0

::list relatives addresses of files and directories to do not remove
::. is the project folder
::this bat shouldn't be removed before its finish
set needed=^
.;^
%clean.bat%;^
README.md;^
ties;^
ties\scripts;^
ties\scripts\arguments.py;^
ties\scripts\calculations.py;^
ties\scripts\HTMLtoXML.py;^
ties\default.py;^
ties\ties.py

:: delete no need folders
cd %repo%
for /r %%i in (. *) do (
	set delete=true
	for %%n in (%needed%) do (
		set fullpath="%repo%%%~n"
		for %%f in (!fullpath!) do set fullpath=%%~ff
		if "!fullpath!" == "%%~fi" set delete=false
	)
	:: pause
	if !delete!==true (
		rmdir /q /s "%%~fi" 2>nul
		del /q /f "%%~fi" 2>nul
		echo deleted %%~fi
	) else (
		echo keept   %%~fi
	)
)
::end with no mesage "The batch file cannot be found."
goto 2>nul &^
del /q /f %fullpath_clean.bat% &^
echo deleted %fullpath_clean.bat% &^
tree "%repo%" /f

endlocal