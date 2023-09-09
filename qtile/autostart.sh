#! /bin/bash
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nitrogen --restore &
picom --config ~/.config/picom/picom.conf &
xrandr --output HDMI-0 --mode 1920x1080 --rate 144 --pos 0x0 --output DP-5 --mode 1366x768 --pos 1920x0 --rate 60 &
solaar &
