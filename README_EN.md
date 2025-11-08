# 🏠 Roommate Bill Splitter

> 🇮🇹 [Versione italiana disponibile qui](README.md)

A Python program to automatically split utility bills based on each roommate's actual presence days, using Google Calendar to track absences.

## 📋 How It Works

The program calculates how much each roommate should pay based on the days they were **actually present** in the apartment. Absences are tracked through Google Calendar events.

### Basic Principle
- **More days present = pay more**
- **More days absent = pay less**
- Fees are split equally among everyone

## 🚀 Initial Setup

### 1️⃣ Create the `calendar_url.txt` file

In the project root, create a file called `calendar_url.txt` containing **only** the public URL of your Google Calendar.

**How to get the URL:**

1. Open [Google Calendar](https://calendar.google.com)
2. Go to **Settings** (⚙️) → **Settings**
3. In the left sidebar, click on the calendar you want to use
4. Scroll down to **"Integrate calendar"**
5. Copy the **Secret address in iCal format**
6. Paste it into the `calendar_url.txt` file

**Example of `calendar_url.txt`:**
```
https://calendar.google.com/calendar/ical/your_calendar_1234567890%40group.calendar.google.com/private-abc123def456/basic.ics
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the program
```bash
python main.py
```

## 📅 How to Configure the Calendar

### Recording Absences

To record an absence, create an event in Google Calendar with these characteristics:

✅ **The event name MUST contain the roommate's name**
   - Examples: `John in London`, `Sarah vacation`, `Mike weekend away`
   
✅ **The event MUST be set as "All day"**
   - When creating the event, check the **"All day"** box
   
✅ **The end date is EXCLUDED**
   - If Mario is away from March 1st to 5th, the event should be set from March 1st to March 6th
   - This way it will count 5 days (1, 2, 3, 4, 5)

### ⚠️ Important

- **Unique name**: Each roommate must have a unique name (no ambiguous abbreviations)
- **All day**: If "All day" is not checked, the event will be ignored
- **Shared calendar**: Make sure all roommates have access to the calendar

### Practical Example

**Scenario**: Luke goes on vacation from January 10th to 15th (5 days)

**How to create the event:**
- Event name: `Luke vacation Spain` (or any text containing "Luke")
- Start date: January 10th
- End date: January 16th (⚠️ important: one day after the last day of absence)
- Check: ✅ All day

## 🖥️ Usage

1. **Run the program**
```bash
   python main.py
```

2. **Fill out the form** that opens in the browser:
   - Bill start date
   - Bill end date
   - Total bill amount
   - Fees (bank charges, etc.)
   - Roommate names (separated by comma)

3. **The program generates a PDF receipt** with:
   - Payment summary for each roommate
   - Absence details
   - Total to pay (share + fee)

## 📊 Output

The program generates a PDF file called `ricevuta_bolletta.pdf` containing:

- 📅 Reference period
- 💰 Total bill and fees
- 📋 Summary table with:
  - Presence days for each roommate
  - Base share calculated proportionally
  - Fee split equally
  - Total to pay
- 📝 Details of all absences for each person

## 🛠️ Requirements

- Python 3.7+
- Public or shared Google Calendar
- Internet connection (to sync the calendar)

## 📁 File Structure
```
project/
├── main.py                  # Main file
├── interfacciaGrafica.py    # HTML interface
├── funcioniCalcoli.py       # Calculation logic
├── calendar_url.txt         # ⚠️ Calendar URL (to be created)
├── requirements.txt         # Dependencies
├── .gitignore              # Files to ignore in Git
└── ricevuta_bolletta.pdf   # Generated output
```

## ❓ FAQ

**Q: Can I use multiple calendars?**  
A: Currently the program supports only one calendar. All events must be in the same calendar.

**Q: What happens if I forget to set "All day"?**  
A: The event will be ignored and those days will be counted as presence.

**Q: What if two people have the same name?**  
A: Use unique names or different abbreviations for each roommate.

## 📝 License

Personal project for shared bill management.

## 🤝 Contributions

Suggestions and improvements are welcome!

---

**Note**: Remember NOT to commit the `calendar_url.txt` file to GitHub (it's already in .gitignore) to protect your calendar's privacy! 🔒