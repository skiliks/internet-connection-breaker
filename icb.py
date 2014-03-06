#! /usr/bin/python3
# -*- coding: utf-8 -*-
import getopt
import sys
import time
import subprocess


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


def main():

    #количество разрывов в одной волне
    brakes_amount = 10

    #время между разрывами
    brakes_pause = 1

    #длительность разрыва
    brakes_duration = 20

    #время между волнами
    wave_pause = 30

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
            brakes_amount = int(a)
        elif o == "--brakes_pause":
            brakes_pause = int(a)
        elif o == "--brakes_duration":
            brakes_duration = int(a)
        elif o == "--wave_pause":
            wave_pause = int(a)
        elif o == "--wave_type":
            wave_type = int(a)
        else:
            print("Name = " + o)
            print("Value = " + a)
            assert False, "unhandled option"

    if brakes_amount % 2 != 0:
        brakes_amount += 1

    while True:
        #одна волна
        i = 0
        while i < brakes_amount:
            subprocess.call(CONNECTION_OFF, shell=True)
            if wave_type == WAVE_TYPE_CONST:
                time.sleep(brakes_duration)
                #print(brakes_duration)
            elif wave_type == WAVE_TYPE_UP:
                time.sleep((i + 1) * (brakes_duration / brakes_amount))
                #print((i + 1) * (brakes_duration / brakes_amount))
            elif wave_type == WAVE_TYPE_DOWN:
                time.sleep((brakes_amount - i) * (brakes_duration / brakes_amount))
                #print((brakes_amount - i) * (brakes_duration / brakes_amount))
            elif wave_type == WAVE_TYPE_HEEL:
                if i < brakes_amount / 2:
                    time.sleep((i + 1) * (brakes_duration / (brakes_amount/2)))
                    #print((i + 1) * (brakes_duration / (brakes_amount/2)))
                else:
                    time.sleep((brakes_amount - i) * (brakes_duration / (brakes_amount/2)))
                    #print((brakes_amount - i) * (brakes_duration / (brakes_amount/2)))
            else:
                assert False, "wave_type - " + wave_type + " not found"
                
            subprocess.call(CONNECTION_ON, shell=True)
            i += 1
            time.sleep(brakes_pause)

        time.sleep(wave_pause)


if __name__ == "__main__":
    main()