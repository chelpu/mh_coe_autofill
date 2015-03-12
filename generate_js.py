import sys

event_name = raw_input('Enter the event name: ');
event_date = raw_input('Enter the date (mm/dd/yyyy): ')
date = event_date.split("/")
if not (len(date) == 3):
    sys.exit("Date is incorrectly formatted")

event_time = raw_input('Enter time time (ex. 7pm): ')
event_location = raw_input('Enter the location: ')
event_shrt_desc = raw_input('Enter shortened event description (200 chars max): ')
if len(event_shrt_desc) > 200:
    sys.exit("Short description is more than 200 characters...")

event_desc = raw_input('Enter the event description: ')

print event_name, event_location

javascript_code = ""

javascript_code += "document.getElementsByClassName('ticketTitleInput')[0].value = '" + event_name + "';\n"
javascript_code += "document.getElementById('DATE_S_MonthInput_Event__bDate_S_Month').value = '" + date[0] + "';\n"
javascript_code += "document.getElementById('DATE_S_DayInput_Event__bDate_S_Day').value = '" + date[1] + "';\n"
javascript_code += "document.getElementById('DATE_S_YearInput_Event__bDate_S_Year').value = '" + date[2] + "';\n"

javascript_code += "document.getElementById('userfield11').value = '" + event_time + "';\n"
javascript_code += "document.getElementById('userfield14').value = '" + event_location + "';\n"
javascript_code += "document.getElementById('userfield7').value = '" + event_shrt_desc + "';\n"
javascript_code += "document.getElementById('descrpt').value = '" + event_desc + "';\n"
javascript_code += "document.getElementById('userfield8').value = 'Workshop';\n"
javascript_code += "document.getElementById('userfield17').value = 'Student__bOrganization';\n"

javascript_code += "document.getElementById('userfield16').value = 'Chelsea Pugh';\n"

print "Run this js in the console of the EECS announcement submission page:"
print javascript_code