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
    brakes_amount = 4

    #время между разрывами (секунды)
    brakes_pause = 2

    #длительность разрыва (секунды)
    brakes_duration = 3

    #время между волнами (секунды)
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

    print("Parameters: \n brakes_amount = ", brakes_amount, "\n brakes_pause = ", brakes_pause, '\n brakes_duration = ',
          brakes_duration, "\n wave_pause = ", wave_pause, "\n wave_type = ", wave_type)

    while True:
        #одна волна
        i = 0
        while i < brakes_amount:
            subprocess.call(CONNECTION_OFF, shell=True)
            print("Connection off at ", datetime.datetime.now().strftime("%H:%M:%S"))
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
                    time.sleep((i + 1) * (brakes_duration / (brakes_amount / 2)))
                    #print((i + 1) * (brakes_duration / (brakes_amount/2)))
                else:
                    time.sleep((brakes_amount - i) * (brakes_duration / (brakes_amount / 2)))
                    #print((brakes_amount - i) * (brakes_duration / (brakes_amount/2)))
            else:
                assert False, "wave_type - " + wave_type + " not found"

            subprocess.call(CONNECTION_ON, shell=True)
            print("Connection on at ", datetime.datetime.now().strftime("%H:%M:%S"))
            i += 1
            time.sleep(brakes_pause)

        time.sleep(wave_pause)


if __name__ == "__main__":
    main()