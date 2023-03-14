#NoTrayIcon
#include <FileConstants.au3> 
#include <Date.au3>

$oldWindow = WinGetTitle("[ACTIVE]")



while 1
    sleep(1000)
    $sText = WinGetTitle("[ACTIVE]")
    if $oldWindow<>$sText Then
        $year = @YEAR
        $month = @MON
        $day = @MDAY
        $date = $year & "-" & $month & "-" & $day
        $logfile= "logs/" & $date & ".log"
        $hFileOpen = FileOpen($logfile, $FO_APPEND)
        $text_to_store = @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC & " | " & $sText
        FileWriteLine($hFileOpen, $text_to_store) 
        $oldWindow=$sText
        FileClose($hFileOpen)
    EndIf 
WEnd



