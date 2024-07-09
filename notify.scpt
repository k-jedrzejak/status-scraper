-- notify.scpt

on run argv
    set messageText to item 1 of argv
    display notification messageText with title "Notification" beep
end run
