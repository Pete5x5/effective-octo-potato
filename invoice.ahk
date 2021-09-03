!+^i::
InvNum := 2
InvEnd := 11
NumLoops := InvEnd - InvNum + 1
Loop, %NumLoops% {
    SendInput, ^p
    Sleep, 3000
    SendInput, {Tab}
    Sleep, 1000
    SendInput, {Enter}
    Sleep, 2000
    SendInput, {Enter}
    Sleep, 2000
    SendInput, %InvNum%
    Sleep, 1000
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
InvNum := 2
SendInput, %InvNum%
Sleep, 500
SendInput, {Enter}
Return
Esc::ExitApp