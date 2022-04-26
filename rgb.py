#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is for RGB colours


def main():
    # this function shows the RGB values

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process & output
    print("")
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("{0}, {1}, {2}".format(counter1, counter2, counter3))
    print("\nDone.")


if __name__ == "__main__":
    main()
