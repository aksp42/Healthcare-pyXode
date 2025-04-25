import time
from plyer import notification
medicines = {}

def add_medicine():
    name = input("Enter the Medicine name : ")
    med_time = input("Enter Time(HH:MM) : ")
    medicines.update({name:med_time})
    print(f"Medicine {name} set for {med_time}.")

def check_medicine():
    while True:
        current_time = time.strftime('%H:%M')
        for med , med_time in medicines.items():
                if current_time == med_time :
                    message = "Reminder! Take your medicine"
                    print(f"Reminder! Take your medicine : {med} ")
                    notification.notify(
                    title="Medicine Reminder",
                    message=message,
                    timeout=15  
                )
                    mark_medicine(med)
        time.sleep(60)
    
                    
def mark_medicine(med):
    Status = input (f"Did you take {med} ? (yes/no) : ").lower()
    
    with open ("Medlog.txt","a") as f:
        
        f.write (f"{med} -> {Status} at {time.strftime('%H:%M')}\n")
    print(f"✅ {med} marked as {'taken' if Status == 'yes' else 'missed'}")
    
def view_history():
    try:
        with open("Medlog.txt","r") as f:
            print("Medicine History ->")
            print(f.read())
    except  FileNotFoundError:
        print("No history is found!")

patient_name = input("Enter User Name: ").strip()
try:
    with open("Medlog.txt", "r") as f:
        file_data = f.read()
except FileNotFoundError:
    file_data = ""
if f"Patient Name: {patient_name}" not in file_data:
    with open ("Medlog.txt","a") as f:
        f.write(f"Patient Name : {patient_name}\n")
        f.write("Medicine History\n")   
while True:
    
    print("Add Medicine(1)\nStart Reminder(2)\nView History(3)\n")
    choice = input("Choose an option (1/2/3/4) : ")
    
    if choice == "1":
        add_medicine()
    elif choice == "2":
        print("Reminder is Set!")
        check_medicine()
    elif choice == "3":
        view_history()
    elif choice == "4":
        print("Stay Healthy!")
        break
    else:
        print("Invalid choice! Please enter 1/2/3")
        
        

    
        
