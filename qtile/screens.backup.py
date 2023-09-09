from libqtile import bar#, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

import os

decoration_group = {
    "decorations": [
        RectDecoration(colour="#546e7a", radius=3, filled=True, padding_y=3, group=True)
    ],
    "padding": 10,
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=4),
                widget.TextBox("⁕⁕⁕", name="default", fontsize=16, **decoration_group),
                widget.GroupBox(highlight_method='text', active='#ff5370', this_current_screen_border='#89ddff', foreground='#8f93a2', fontsize=15),
                widget.CurrentLayout(fmt='[{}]', foreground='#8f93a2'),
                #widget.Prompt(),
                #widget.Spacer(bar.STRETCH),
                widget.TaskList(border='#546e7a', borderwidth=3, highlight_method='block', margin_y=2, max_title_width=200, padding_x=10),
                #widget.Spacer(bar.STRETCH),
                widget.Chord(
                    chords_colors={
                        "launch": ("#89ddff", "#ff5370"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                #widget.CheckUpdates(),
                widget.Spacer(length=8),
                widget.Clock(format='%d/%m/%y', **decoration_group),
                widget.Spacer(length=8),
                widget.Clock(format="%H:%M", **decoration_group),
                widget.Spacer(length=8),
                widget.TextBox("  ", fontsize=16, mouse_callbacks={'Button1': lazy.spawn(os.path.expanduser("~/scripts/custom/powermenu.sh"))}, **decoration_group),
                widget.Spacer(length=4),

                #widget.QuickExit(default_text='[󰐥]', fontsize=18, countdown_format='[{}]'),
            ],
            25,
            background='#0f111a',
            # opacity=0.8, # margin=[10, 8, 0, 8], 
            border_width=[0, 0, 1, 0],  # Draw top and bottom borders
            border_color=["000000", "000000", "89ddff", "000000"],  # Borders are magenta
        ),
    ),
]
