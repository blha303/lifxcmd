#!/usr/bin/env python3
import lifxlan
import argparse
import sys
import re

l = lifxlan.LifxLAN()

def fix_color(arg_color):
    if arg_color.count(",") == 1:
        arg_color, K = arg_color.split(",")
    else:
        K = 9000
    try:
        H,S,B = (int(group,16) for group in re.match(r'(....)(....)(....)', arg_color).groups())
    except (ValueError,AttributeError):
        try:
            import colour
        except ImportError:
            raise Exception("Invalid input on --color: {} does not match HHHHSSSSBBBB,KKKK and you do not have colour installed")
        try:
            color = colour.Color(arg_color)
        except ValueError as e:
            raise Exception("Invalid input on --color: " + e.args[0])
        H,S,B = map(lambda x: x*65535, color.get_hsl())
    return [H,S,B,K]
                

def main():
    parser = argparse.ArgumentParser(prog="lifxcmd")
    parser.add_argument("-b", "--light", help="Specify which comma-separated light(s) to act on. If unset, acts on all lights found on the LAN via broadcast")
    parser.add_argument("-B", "--list-lights", help="List all lights newline separated to stdout", action="store_true")
    parser.add_argument("-p", "--power", help="Set power on/off", choices={"on","off"})
    parser.add_argument("-P", "--toggle-power", help="Toggle power on all specified lights (i.e on>off, off>on). Useful for moving between rooms maybe", action="store_true")
    parser.add_argument("-c", "--color", help="""
    Specify color in form HHHHSSSSBBBB,KKKK, where H,S,B are hexadecimal and K is an optional decimal between 2500 and 9000 defaulting to 9000, representing hue/saturation/brightness/Kelvin.
    Alternatively, install colour from pip and use any string it supports. You can still specify Kelvin with `,KKKK` after a given word, as colour does not support Kelvin.
    Keep in mind that setting color does not affect power, you'll still need to turn power on.""")
    parser.add_argument("-g", "--get-color", help="Prints current color for minor edits", action="store_true")
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()
    args = parser.parse_args()
    if args.color is not None:
        color = fix_color(args.color)
    else:
        color = None

    if not args.light and args.power is not None:
        # fast mode
        if color:
            l.set_color_all_lights(color, rapid=True)
        l.set_power_all_lights(args.power, rapid=True)
        return 0

    # slow mode
    l.discover_devices()
    if args.get_color:
        for light in l.devices:
            H,S,B,K = light.get_color()
            H,S,B = map(lambda x: hex(x)[2:].zfill(4),(H,S,B))
            print("{}: {}{}{},{}".format(light.get_label(), H,S,B,K))
    if args.list_lights:
        print("\n".join(light.get_label() for light in l.devices))
        return 0

    if args.light:
        lights = [light for light in l.devices if light.get_label() in args.light.split(",")]
    else:
        lights = l.devices

    if args.toggle_power:
        for light in lights:
            light.set_power(not light.get_power())
    elif args.power is not None:
        for light in lights:
            light.set_power(args.power)

    return 0

if __name__ == "__main__":
    sys.exit(main())
