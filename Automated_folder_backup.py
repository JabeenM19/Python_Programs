import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\DELL\Pictures\Screenshots"
Destination_dir = r"C:\Users\DELL\Desktop\backups"

def copy_folder_to_directory(source,destination):
    today =  datetime.date.today()
    Destination_dir = os.path.join(destination,str(today))
    CLEAR ="\033[2J"
    print(CLEAR)
    try:
        shutil.copytree(source, Destination_dir)
        print(f"Folder copied to:{Destination_dir}")
    except FileExistsError:
        print(f"Folder already exists in:{destination}")

schedule.every().day().at("9:00").do(lambda: copy_folder_to_directory(source_dir,Destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
    