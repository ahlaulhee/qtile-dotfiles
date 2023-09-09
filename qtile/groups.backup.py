from libqtile.config import Group, Match

group_names = ["1", "2", "3", "4", "5", "6"]
group_labels = ["󰋘", "󰋘", "󰋘", "󰋘", "󰋘", "󰋘"]

groups = [Group(name, label=label) for name, label in zip(group_names, group_labels)]

#assign = [
#    Match(wm_class=['discord'], target='4'),
#    Match(wm_class=['slack-desktop'], target='4'),
#    Match(wm_class=['spotify'], target='5'),
#    Match(wm_class=['solaar'], target='6'),
#]

#for i in groups:
#    matches = [match for match in assign if match.target == i.name]
#    if matches:
#        i.matches = matches
