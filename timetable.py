from bs4 import BeautifulSoup
with open("timetable.html","r") as timetable:
    soup = BeautifulSoup(timetable.read(), 'html.parser')


days = ["MON","TUE","WED","THU","FRI","SAT"]
days1 = ["TUE","WED","THU","FRI","SAT"]

timeT = {

    1: "8:00-8:50",
    2: "9:00-9:50",
    3: "9:00-9:50",
    4: "10:00-10:50",
    5: "10:00-10:50",
    6: "11:00-11:50",
    7: "11:00-11:50",
    8: "12:00-12:50",
    9: "12:00-12:50",
    10: "13:00-13:50",
    11: "LUNCH",
    12: "14:00-14:50",
    13: "14:00-14:50",
    14: "15:00-15:50",
    15: "15:00-15:50",
    16: "16:00-16:50",
    17: "16:00-16:50",
    18: "17:00-17:50",
    19: "17:00-17:50",
    20: "18:00-18:50",
    21: "19:00-19:50"

}


timetable = {}

for str in soup.stripped_strings:
    if str in days:
        timetable[str] = []
            
    if str == "SAT":
        break

results = soup.findAll("td")

for j in days:
    for i in results:

        if len(i.string) >7:
            timetable[j].append({"class":i.string})
            results.remove(i)
        if i.string in days1:
            results.remove(i)
            break

print(timetable)


