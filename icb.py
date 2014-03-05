#! /usr/bin/python3
# -*- coding: utf-8 -*-
import getopt
import sys
import time
import subprocess


def main():
    #команда включения интернета
    CONNECTION_ON = "echo 'on'"
    #команда выключения интернета
    CONNECTION_OFF = "echo 'off'"
    #равномерная длительность разрыва
    WAVE_TYPE_CONST = "const"
    #длительность разрыва увеличивается от нуля до ДР к концу волны
    WAVE_TYPE_UP = "up"
    #длительность разрыва уменьшается от ДР до нуля к концу волны
    WAVE_TYPE_DOWN = "down"
    #длительность разрыва нарастает от нуля к ДР (в середине волны) и спадает до нуля к концу
    WAVE_TYPE_HEEL = "heel"
    #количество разрывов в одной волне
    brakes_amount = 4

    #время между разрывами
    brakes_pause = 2

    #длительность разрыва
    brakes_duration = 2

    #время между волнами
    wave_pause = 3

    #тип волны
    wave_type = WAVE_TYPE_CONST

    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["brakes_amount=", "brakes_pause=", "brakes_duration=", "wave_pause=", "wave_type="])
    except getopt.GetoptError as err:
        print(err)

        sys.exit(2)
    for o, a in opts:
        if o == "--brakes_amount":
            brakes_amount = a
        elif o == "--brakes_pause":
            brakes_pause = a
        elif o == "--brakes_duration":
            brakes_duration = a
        elif o == "--wave_pause":
            wave_pause = a
        elif o == "--wave_type":
            wave_type = a
        else:
            print("Name = "+o)
            print("Value = "+a)
            assert False, "unhandled option"
            # ...

    #while True:
    i = 0
    while i < 2:
        subprocess.call(CONNECTION_ON, shell=True)
        #time.sleep(3)
        i += 1
        print(i)
        print(brakes_amount)

if __name__ == "__main__":
    main()