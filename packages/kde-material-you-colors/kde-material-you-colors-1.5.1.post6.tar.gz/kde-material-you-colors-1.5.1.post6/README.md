<div align="center">

# 🎨 KDE Material You Colors

## Automatic Material You Colors Generator from your wallpaper for the Plasma Desktop

This is a Python program that uses the [Python implementation](https://github.com/avanishsubbiah/material-color-utilities-python) of Google's [Material Color Utilities](https://github.com/material-foundation/material-color-utilities) to generate a Material Design 3 color scheme.
Which is used to generate Light and Dark Color Themes for KDE (and pywal if installed) from your current wallpaper, automatically.

![](https://img.shields.io/static/v1?style=for-the-badge&label=Made%20with&message=Python&color=1f425f&logo=python&labelColor=2d333b)
![](https://img.shields.io/github/v/release/luisbocanegra/kde-material-you-colors?include_prereleases&style=for-the-badge&color=1f425f&labelColor=2d333b)
</div>

<div>
<img src="https://user-images.githubusercontent.com/15076387/188578458-8171e42b-f36c-44c1-9eb0-506c301d4f16.gif"  alt="Screenshot">
</div>

# Features

## Plasma specific

- Update automatically on wallpaper change
- Multiple wallpaper [plugins supported](#working-wallpaper-plugins)
- Support for selecting Wallpaper plugin from secondary monitors
- Dark and Light Icon theme
- Support Plasma 5.26+ dark wallpaper variants
- Start automatically on login
- Make titlebar darker to match specified applications like terminals, code editors and other programs themed by pywal
- Follow Plasma Material You Dark/Light change to work with theme schedulers like [Koi](https://github.com/baduhai/Koi)
- **Plasma addons**
  - Tint [SierraBreeze](https://github.com/kay0u/SierraBreeze) window decoration buttons
  - TitleBar opacity control for [Klassy](https://github.com/paulmcauley/klassy) and [SierraBreezeEnhanced](https://github.com/kupiqu/SierraBreezeEnhanced) window decorations
  - ToolBar opacity control for [Lightly](https://github.com/Luwx/Lightly) Application style
  - Tint [Klassy](https://github.com/paulmcauley/klassy) window decoration outline

## Themeable programs

- Konsole color scheme
  - opacity control
- **[Pywal](https://github.com/dylanaraps/pywal) support to theme other programs using Material You Colors**
- Basic KSyntaxHighlighting support (Kate, KWrite, KDevelop...)

## Theming options

- Alternative Material You color selection if the wallpaper provides more than one
- Use your favorite color to generate Material You color schemes
- Custom colors list used for konsole/pywal
- Custom amount for background color tint
- Dark/light Color schemes (Plasma and pywal/konsole independently)
- Set a script/command that will be executed on start or wallpaper/dark/light/settings change
- Configuration file

# Installing

## Using pypi

```sh
pip install kde-material-you-colors
# Optional
# pywal to theme other programs using Material You Colors
pip install pywal
# Colr to display colored palette and seed colors from terminal (approximate)
pip install colr
```

## Arch Linux

- [AUR](https://aur.archlinux.org/packages/kde-material-you-colors) use your preferred AUR helper

## openSUSE Build Service packages by [marknefedov](https://github.com/marknefedov)

### Fedora

Add repository and install as root:

```sh
dnf config-manager --add-repo https://download.opensuse.org/repositories/home:MarkNefedov/Fedora_37/home:MarkNefedov.repo
dnf install kde-material-you-colors
```

### openSUSE

For **openSUSE Tumbleweed** add repository and install as root:

```sh
zypper addrepo https://download.opensuse.org/repositories/home:MarkNefedov/openSUSE_Tumbleweed/home:MarkNefedov.repo
zypper refresh
zypper install kde-material-you-colors
```

For **openSUSE 15.4** add repository and install as root:

```sh
zypper addrepo https://download.opensuse.org/repositories/home:MarkNefedov/15.4/home:MarkNefedov.repo
zypper refresh
zypper install kde-material-you-colors
```

## Optional features

- Install the [Colr](https://pypi.org/project/Colr/) python module to display colored palette and seed colors from terminal
- Install the [pywal](https://pypi.org/project/pywal/) python module to theme other programs using Material You Colors
  - Check [pywal Customization Wiki](https://github.com/dylanaraps/pywal/wiki/Customization) to theme supported programs

# Running from terminal to debug your configuration

- Run `kde-material-you-colors`

- Flags take precedence over sonfiguration file, run `kde-material-you-colors -h` to see the list of available options

## Starting/Stopping Desktop entries

Run `kde-material-you-colors -cl` to copy desktop entries to ~/.local/share/applications/:

- To start the program launch **KDE Material You Colors** from your applications list
- To stop it launch **Stop KDE Material You Colors** from your applications list

# Running on Startup

After finishing the setup, you can make it run automatically on boot

1. Copy the default configuration to ~/.config/kde-material-you-colors/config.conf:

    `kde-material-you-colors -c`

2. Set the program to automatically start with Plasma:

    `kde-material-you-colors -a`

3. Reboot or logout/login and test the changes

## Removing from autostart

1. Open `System Settings` > `Startup and Shutdown`
2. Remove `kde-material-you-colors` by clicking on the `-` button.

# Working Wallpaper plugins

**Wallpaper plugins must store the current wallpaper in `~/.config/plasma-org.kde.plasma.desktop-appletsrc`**

Confirmed working Plasma Wallpaper Plugins:

| Name | ID |
| ----------- | ----------- |
| Image (default) | `org.kde.image` |
| Picture of the day | `org.kde.potd` |
| Slideshow | `org.kde.slideshow` |
| Plain color | `org.kde.color` |
| Conway's Game of Life (cell color) | `org.kde.plasma.gameoflife` |
| Active blur | `a2n.blur` |

# Configuration file

- Copy default configuration: run `kde-material-you-colors -c`
- Edit ~/.config/kde-material-you-colors/config.conf
- Run `kde-material-you-colors` with no arguments from terminal to test it.
- **You can view the sample configuration file [here](https://github.com/luisbocanegra/kde-material-you-colors/blob/plasmoid/src/kde_material_you_colors/data/sample_config.conf)**

# Notes

- To update color with `plasma-apply-colorscheme` (utility provided by plasma developers), the file containing the new color scheme must have a different name than the current one, to workaround this the program creates two scheme files with different names, then applies one after the other. As a result you end up with duplicated color schemes and maybe some lag while updating schemes.

## Bug reporting / Feature requests / Contributing

Please read the [Contributing guidelines in this repository](CONTRIBUTING.md)

# Thanks & Credits

- [Avanish Subbiah](https://github.com/avanishsubbiah) for the [Python implementation](https://github.com/avanishsubbiah/material-color-utilities-python) of Material Color Utilities required by this project.
- [This comment by throwaway6560192 on Reddit](https://www.reddit.com/r/kde/comments/mg6wr4/comment/gssbtqe/?utm_source=share&utm_medium=web2x&context=3) and [@pashazz  (Pavel Borisov) ksetwallpaper](https://github.com/pashazz/ksetwallpaper) for the script to get the current Wallpaper that served me as starting point.
- Everyone that made [material-color-utilities](https://github.com/material-foundation/material-color-utilities) possible.
- [Pywal](https://github.com/dylanaraps/pywal) developers
- [Albert Ragány-Németh](https://github.com/albi005) for the [C# implementation](https://github.com/albi005/MaterialColorUtilities) of Material Color Utilities (used until v0.8.0).
