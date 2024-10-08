from ics import Calendar, Event
import datetime
from bs4 import BeautifulSoup
import pytz  

with open("timetable.html", "r") as timetable_file:
    soup = BeautifulSoup(timetable_file.read(), 'html.parser')


ist = pytz.timezone('Asia/Kolkata')

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]
days1 = ["TUE", "WED", "THU", "FRI", "SAT"]

timeS = {
    3: '8:00', 4: '9:00', 5: '9:00', 6: '10:00', 7: '10:00', 
    8: '11:00', 9: '11:00', 10: '12:00', 11: '12:00', 12: '13:00', 
    14: '14:00', 15: '14:00', 16: '15:00', 17: '15:00', 
    18: '16:00', 19: '16:00', 20: '17:00', 21: '17:00', 
    22: '18:00', 23: '19:00'
}

timeE = {
    3: '8:50', 4: '9:50', 5: '9:50', 6: '10:50', 7: '10:50', 
    8: '11:50', 9: '11:50', 10: '12:50', 11: '12:50', 12: '13:50', 
    14: '14:50', 15: '14:50', 16: '15:50', 17: '15:50', 
    18: '16:50', 19: '16:50', 20: '17:50', 21: '17:50', 
    22: '18:50', 23: '19:50'
}

timetable = {}
counter = 3

def create_raw():
    global counter
    for str in soup.stripped_strings:
        if str in days:
            timetable[str] = []

        if str == "SAT":
            break

    results = soup.findAll("td")
    processed_indices = set()

    for j in days:
        for index, i in enumerate(results):
            if index in processed_indices:
                continue

            if i.string and len(i.string) > 7:
                if counter in timeS and counter in timeE:
                    timetable[j].append({"start-time": timeS[counter], "end-time": timeE[counter], "class": i.string})
                    processed_indices.add(index)

            if i.string == "THEORY" or i.string == "LAB":
                counter = 3
            else:
                counter += 1
                if counter not in timeS or counter not in timeE:  
                    counter = 3
                

            if i.string in days1:
                processed_indices.add(index)
                break
    print(timetable)
    create_ics()
    

def create_ics():
    cal = Calendar()
    start_date = datetime.datetime.now().date()

    for key, value in timetable.items():
        for i in value:
            event = Event()  
            event.name = i['class']
            print(f"Event: {i['class']}, Start: {i['start-time']}, End: {i['end-time']}")
            
            
            event_begin = datetime.datetime.strptime(f"{start_date} {i['start-time']}", '%Y-%m-%d %H:%M')
            event_end = datetime.datetime.strptime(f"{start_date} {i['end-time']}", '%Y-%m-%d %H:%M')
            
            
            event.begin = ist.localize(event_begin)
            event.end = ist.localize(event_end)
            
            cal.events.add(event)

        start_date += datetime.timedelta(days=1)

    
    with open('timetable.ics', 'w') as f:
        f.writelines(cal)

create_raw()