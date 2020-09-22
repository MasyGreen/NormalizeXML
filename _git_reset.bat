rem Удалить локальные изменения, синхронизировать с удаленным
pause
git fetch origin
git reset --hard origin/master
git clean -f -d