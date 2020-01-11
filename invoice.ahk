!+^i::
InvNum := 7
InvEnd := 35
NumLoops := InvEnd - InvNum + 1
Loop, %NumLoops% {
    SendInput, ^p
    Sleep, 3000
    SendInput, {Tab}
    Sleep, 3000
    SendInput, {Enter}
    Sleep, 3000
    SendInput, {Enter}
    Sleep, 3000
    InvNum += 1
    SendInput, {Delete}
    Sleep, 500
    SendInput, %InvNum%
    Sleep, 500
    SendInput, {Enter}
    Sleep, 500
    SendInput, {Up}
    Sleep, 500
}
SendInput, {Del}
Sleep, 500
InvNum := 7
SendInput, %InvNum%
Sleep, 500
SendInput, {Enter}
Return
Esc::ExitApp