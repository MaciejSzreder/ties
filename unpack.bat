:<<::cmd
	@echo off
	setlocal EnableDelayedExpansion
::cmd

:;#list relatives addresses of files and directories to do not remove
# 2>nul &set ^
needed=(^
 .^
 README.md^
 ties^
 ties/scripts^
 ties/scripts/arguments.py^
 ties/scripts/calculations.py^
 ties/scripts/HTMLtoXML.py^
 ties/default.py^
 ties/ties.py^
)

:<<::cmd
	::get path of folder with project
	set repo=%~dp0
	::get this bat adress
	set clean.bat=%~nx0
	set fullpath_clean.bat=%~f0

	::remove brackets
	set needed=%needed:~1,-1%
	::use proper slash
	set needed=%needed:/=\%
	::to avoid mesage "The batch file cannot be found."
	set needed=%needed% %clean.bat%

	:: delete no needed folders and files
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
	::end with no 
	goto 2>nul ^
	& echo deleted %fullpath_clean.bat%^
	& del /q /f "%fullpath_clean.bat%"^
	& echo. ^
	& tree "%repo%" /f^
	& endlocal
::cmd

	#animation images have to fit in one row
	anim=( \| / - \\ )
	anim_i=0
	
	repo=`dirname "\`realpath "$0"\`"`

	#remove ^
	needed=${needed[*]%?}
	#use proper slash
	needed=${needed[*]//\\//}
	
	shopt -s globstar
	shopt -s dotglob
	cd=`pwd`
	cd "$repo"
	for f in **
	do
		if printf "%s\0" "${needed[*]}" | grep -z -q "$f"
		then
			echo "keept   $f"
		else
			if [[ -e "$f" ]]
			then
				echo "deleted $f"
				rm -rf "$f"
			else
				printf "%s\r" "${anim[$((anim_i++%${#anim[*]}))]}"
			fi
		fi
	done
	
	cd "$cd"
	
	echo
	(tree -a "$repo" ||
	tree.com //a //f "$repo" ||
	gio tree -h "$repo" ||
	gvfs-tree -h "repo" ||
	find %repo | sed -e "s/[^-][^\/]*\//  |/g" -e "s/|\([^ ]\)/|-\1/"
	)2>/dev/null

#sources
# - https://www.codegrepper.com/code-examples/shell/linux+alternatives+to+tree