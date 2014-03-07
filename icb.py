#! /usr/bin/python3
# -*- coding: utf-8 -*-
import getopt
import sys
import time
import datetime
import subprocess

connection_name = "Подключение по локальной сети"
#netsh interface set interface "Подключение по локальной сети" admin=DISABLED
#команда включения интернета
CONNECTION_ON = 'netsh interface set interface "' + connection_name + '" admin=ENABLED'
#команда выключения интернета
CONNECTION_OFF = 'netsh interface set interface "' + connection_name + '" admin=DISABLED'
#равномерная длительность разрыва
WAVE_TYPE_CONST = "const"
#длительность разрыва увеличивается от нуля до ДР к концу волны
WAVE_TYPE_UP = "up"
#длительность разрыва уменьшается от ДР до нуля к концу волны
WAVE_TYPE_DOWN = "down"
#длительность разрыва нарастает от нуля к ДР (в середине волны) и спадает до нуля к концу
WAVE_TYPE_HEEL = "heel"


def main():
    #константы по умолчанию
    #количество разрывов в одной волне
    breaks_amount = 4

    #время между разрывами (секунды)
    breaks_pause = 2

    #длительность разрыва (секунды)
    breaks_duration = 3

    #время между волнами (секунды)
    wave_pause = 30

    #тип волны
    wave_type = WAVE_TYPE_CONST

    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["breaks_amount=", "breaks_pause=", "breaks_duration=", "wave_pause=", "wave_type="])
    except getopt.GetoptError as err:
        print(err)

        sys.exit(2)
    for o, a in opts:
        if o == "--breaks_amount":
            breaks_amount = int(a)
        elif o == "--breaks_pause":
            breaks_pause = int(a)
        elif o == "--breaks_duration":
            breaks_duration = int(a)
        elif o == "--wave_pause":
            wave_pause = int(a)
        elif o == "--wave_type":
            wave_type = a
        else:
            print("Name = " + o)
            print("Value = " + a)
            assert False, "unhandled option"

    if breaks_amount % 2 != 0:
        breaks_amount += 1

    print("Parameters: \n breaks_amount = ", breaks_amount, "\n breaks_pause = ", breaks_pause, '\n breaks_duration = ',
          breaks_duration, "\n wave_pause = ", wave_pause, "\n wave_type = ", wave_type)

    while True:
        #одна волна
        i = 0
        while i < breaks_amount:
            subprocess.call(CONNECTION_OFF, shell=True)
            print("Connection off at ", datetime.datetime.now().strftime("%H:%M:%S"))
            if wave_type == WAVE_TYPE_CONST:
                time.sleep(breaks_duration)
                #print(breaks_duration)
            elif wave_type == WAVE_TYPE_UP:
                time.sleep((i + 1) * (breaks_duration / breaks_amount))
                #print((i + 1) * (breaks_duration / breaks_amount))
            elif wave_type == WAVE_TYPE_DOWN:
                time.sleep((breaks_amount - i) * (breaks_duration / breaks_amount))
                #print((breaks_amount - i) * (breaks_duration / breaks_amount))
            elif wave_type == WAVE_TYPE_HEEL:
                if i < breaks_amount / 2:
                    time.sleep((i + 1) * (breaks_duration / (breaks_amount / 2)))
                    #print((i + 1) * (breaks_duration / (breaks_amount/2)))
                else:
                    time.sleep((breaks_amount - i) * (breaks_duration / (breaks_amount / 2)))
                    #print((breaks_amount - i) * (breaks_duration / (breaks_amount/2)))
            else:
                assert False, "wave_type - " + wave_type + " not found"

            subprocess.call(CONNECTION_ON, shell=True)
            print("Connection on at ", datetime.datetime.now().strftime("%H:%M:%S"))
            i += 1
            time.sleep(breaks_pause)

        time.sleep(wave_pause)


if __name__ == "__main__":
    main()