import time
import random
import curses
from curses import wrapper



def start_scr(stdscr):
    stdscr.clear()
    stdscr.addstr("Press Enter to start")
    stdscr.refresh()
    stdscr.getkey()


def load_text():
    try:
        with open("text.txt", "r") as f:
            lines = f.readlines()
            if lines:
                return random.choice(lines).strip()
    except FileNotFoundError:
        return "This is the default text because the file was not found"
    
curses.start_color()
correct_color= curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
wrong_color = curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) 


def display_text(stdscr,current_text ,target_txt,wps):
    stdscr.addstr(target_txt)
    stdscr.addstr(f"WPS:{wps}")

    for index, char in enumerate(current_text):
        correct_char = target_txt[index]
        if correct_char == target_txt:
            color = curses.color_pair(1)
        else:
            color = curses.color_pair(2)
    stdscr.addstr(index,char,color)
