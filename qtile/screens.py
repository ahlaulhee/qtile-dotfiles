from libqtile import bar#, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from libqtile.bar import CALCULATED

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

import os

decoration_group = {
    "decorations": [
        RectDecoration(colour="#0f111a", radius=8, filled=True, padding_y=3, group=True)
    ],
    "padding": 10,
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    hide_unused=True,
                    disable_drag=True,
                    toggle=False,
                    highlight_method="block",
                    borderwidth=4,
                    this_current_screen_border='#89ddff',
                    block_highlight_text_color='#000000',
                    other_current_screen_border='#ff5370',
                    other_screen_border='#ff5370',
                    active='#FFFFFF',
                    urgent_alert_method="block",
                    urgent_border='#ff5370',
                    urgent_text='#FFFFFF',
                    spacing=4,
                    margin_x=6,
                    margin_y=3,
                    padding_x=2,
                    padding_y=2,
                    **decoration_group 
                ),
                widget.Spacer(length=4),
                widget.CurrentLayout(fmt='[{}]', foreground='#FFFFFF', **decoration_group),
                widget.Spacer(),
                widget.WindowName(width=CALCULATED, max_chars=60, **decoration_group),
                #widget.TaskList(border='#0f111a', highlight_method='block', max_title_width=200, **decoration_group),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#89ddff", "#ff5370"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Spacer(length=8),
                widget.Volume(
                    get_volume_command=os.path.expanduser(
                                "~/.config/qtile/scripts/get-volume.sh"
                            ),
                    fmt=" {:>4}",
                    # mute_text="Mute",
                    mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
                    **decoration_group 
                ),
                widget.Spacer(length=8),
                widget.Clock(format='%d/%m/%y', **decoration_group),
                widget.Clock(format="%H:%M", **decoration_group),
                widget.Spacer(length=8),
                widget.TextBox("  ", fontsize=16, mouse_callbacks={'Button1': lazy.spawn(os.path.expanduser("~/scripts/custom/powermenu.sh"))}, **decoration_group),
            ],
            30,
            background='#00000000',
            opacity=1,
            margin=[4, 8, 0, 8], 
        ),
    ),
]
