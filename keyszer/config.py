#  gsettings set org.gnome.shell.extensions.pop-shell activate-launcher "['<Super>space']"

timeouts(multipurpose = 1)

keymap(
    "Terminal",
    {
        # Protect Terminal weirdness copy-paste
        K("Super-c"): K("Super-c"),
        K("Super-v"): K("Super-v"),
        # Protect new tab/close tab
        K("Super-w"): K("Super-w"),
        K("Super-t"): K("Super-t"),
    },
    when = wm_class_match("Gnome-terminal")
)

keymap(
    "Default",
    {
        # Random expectations
        K("Super-q"): K("C-q"),
        K("Super-l"): K("C-l"),
        K("Super-r"): K("C-r"),
        # Tabs
        K("Super-t"): K("C-t"),
        K("Super-Shift-t"): K("C-Shift-t"),
        K("Super-w"): K("C-w"),
        K("Super-n"): K("C-n"),
        K("Super-Shift-p"): K("C-Shift-p"),
        # Save
        K("Super-s"): K("C-s"),
        # Comment
        K("Super-slash"): K("C-slash"),
        K("Super-s"): K("C-s"),
        # Copy/Paste
        K("Super-c"): K("C-c"),
        K("Super-v"): K("C-v"),
        K("Super-x"): K("C-x"),
        # Undo/Redo
        K("Super-z"): K("C-z"),
        K("Super-Shift-z"): K("C-Shift-z"),
        # Navigation
        K("Alt-Left"): K("C-Left"),
        K("Shift-Alt-Left"): K("Shift-C-Left"),
        K("Alt-Right"): K("C-Right"),
        K("Shift-Alt-Right"): K("Shift-C-Right"),
        K("Super-Left"): K("Home"),
        K("Shift-Super-Left"): K("Shift-Home"),
        K("Super-Right"): K("End"),
        K("Shift-Super-Right"): K("Shift-End"),
        # Select all
        K("Super-a"): K("C-a"),
    },
)
