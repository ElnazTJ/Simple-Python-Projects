import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    song="seven_nation_army.mp3"
    is_running = True
    while is_running:
        now = datetime.datetime.now()
        print(f"Current time: {now.strftime('%H:%M:%S')}")
        if now.strftime('%H:%M:%S') == alarm_time:
            print("----------------------------------------------------")
            print("You're gonna fight them all! so you have to wake up!")
            print("----------------------------------------------------")

            pygame.mixer.init()
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False

        time.sleep(1)



if __name__ =="__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)