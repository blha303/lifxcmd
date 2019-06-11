lifxcmd
=======

A Python program that allows easy control of all bulbs on a network, or a specific bulb if required. Should support any version of Python supported by lifxlan. Please let me know in an issue if this isn't the case.

Installation
------------

`pip install git+https://github.com/blha303/lifxcmd.git#egg=lifxcmd`

lifxcmd features optional support for [colour](https://pypi.org/project/colour/) to resolve arbitrary color strings. To use this, add `[COLOUR]` to the package name above (or install colour separately):

`pip install git+https://github.com/blha303/lifxcmd.git#egg=lifxcmd[COLOUR]`

Usage
-----

```
usage: lifxcmd [-h] [-b LIGHT] [-B] [-p {off,on}] [-P] [-c COLOR] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -b LIGHT, --light LIGHT
                        Specify which comma-separated light(s) to act on. If
                        unset, acts on all lights found on the LAN via
                        broadcast
  -B, --list-lights     List all lights newline separated to stdout
  -p {off,on}, --power {off,on}
                        Set power on/off
  -P, --toggle-power    Toggle power on all specified lights (i.e on>off,
                        off>on). Useful for moving between rooms maybe
  -c COLOR, --color COLOR
                        Specify color in form HHHHSSSSBBBB,KKKK, where H,S,B
                        are hexadecimal and K is an optional decimal between
                        2500 and 9000 defaulting to 9000, representing
                        hue/saturation/brightness/Kelvin. Alternatively,
                        install colour from pip and use any string it
                        supports. You can still specify Kelvin with `,KKKK`
                        after a given word, as colour does not support Kelvin.
                        Keep in mind that setting color does not affect power,
                        you'll still need to turn power on.
  -g, --get-color       Prints current color for minor edits
```
