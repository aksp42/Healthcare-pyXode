# 💊 Medicine Reminder System

## 📌 Project Overview
This Python-based desktop app helps users manage and track their medicine intake by sending notifications at specific times. It also logs whether the medicine was taken or missed.

## 🧠 Features
- Add multiple medicines with reminder times
- Real-time check every minute
- Sends desktop notifications using `plyer`
- Logs responses (yes/no) to `Medlog.txt`
- Tracks medicine history

## 🔧 Technologies Used
- Python
- `time` module
- `plyer` for desktop notifications
- File I/O for log history

## 🛠️ How to Run
1. Make sure you have `plyer` installed:
   ```bash
   pip install plyer

## 📌 1. Adding a Medicine

![Adding a Medicine](screenshot1.png)  
User enters the medicine name and desired reminder time.

---

## ⏰ 2. Starting the Reminder

![Starting the Reminder](screenshot2.png)  
The system confirms that the reminder is successfully set.

---

## 🔔 3. Desktop Notification

![Desktop Notification](screenshot3.png)  
At the specified time, a Windows notification pops up reminding the user to take the medicine.
