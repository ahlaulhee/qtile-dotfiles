from libqtile import layout

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Bsp(
        margin=8,
        border_width=2, 
        border_on_single=True,
        border_focus='#ffffff', #prev: #89ddff
        border_normal='#0f111a',
    ),
    layout.Max(
        border_width=1,
        margin=8,
        border_focus='#ffffff', #prev: #89ddff
        border_normal='#0f111a',
    ),
    # layout.Stack(num_stacks=2),
    #layout.Floating(
    #    border_focus='#89ddff',
    #    border_normal='#0f111a',
    #    border_width=3
    #),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
