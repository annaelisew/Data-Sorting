import csv, sys

def main():
    attendees = {}
    count = 0
    for arg in sys.argv[1:]:
    #sort through spreadsheets
        with open(arg, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                fullname = row[0]
                event = row[3][:12]
                temp = attendees.get(fullname, [])
                if not event in temp:
                    temp.append(event)
                attendees[fullname] = temp
    
    num_attendees = {}
    num_event = {}
        
    for key in attendees:
        num_att = len(attendees[key])
        num_attendees[num_att] = num_attendees.get(num_att, 0) + 1
        if num_att>1:
            count = count+1
        for event in attendees[key]:
            num_event[event] = num_event.get(event, 0) + 1

    print(num_event)
    print(num_attendees)
    print(count)
    
    return 0


if __name__ == "__main__":
  main()
  
