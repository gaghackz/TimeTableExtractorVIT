# timeTableExtractorVIT
Helps converting your VTOP timetable into an ics format so you can import it in your calender apps

special thanks to [Bharat1910](https://github.com/Bharath1910)

# How to use this code:

## STEP 1:

go to your VTOP timetable and right click on the timetable part and click on "Inspect" 

then hover over the code which appears on the right and check every block until you see the whole timetable get highlighted in blue 

when you find that code, right click on that code and click on copy --> copy outerHTML

https://github.com/user-attachments/assets/90efb12b-b699-4889-b2f7-532125b59b94

## STEP 2

now paste that html you copied in a html file named as "timetable.html" and save it in the same folder as timetable.py

## STEP 3

now run timetable.py you should see a file timetable.ics show up in the same folder if the code executed with no errors

## STEP 4

now go to https://calender.google.com and click on settings and make sure your timetzone is set to IST (GMT +5:30) 

now check the bottom left side for "imports/exports" and upload your ics file there and click on import

# YOUR TIMETABLE SHOULD BE SUCCESFULLY IMPORTED INTO GOOGLE CALENDER BY NOW!!
