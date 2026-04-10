# 📋 WhatsApp Daily Task Report Tool

A simple and professional **Python + Streamlit** web app to create a **daily task report message** and send it directly through **WhatsApp**.

This tool helps employees, interns, students, and team members quickly generate a clean daily work update with:

* **Date**
* **Name**
* **Task Performed**
* **In-Time**
* **Lunch Break**
* **Out-Time**
* **Total Working Time (Auto Calculated)**
* **Direct WhatsApp Send Button**

---

## 🚀 Features

* Clean and easy-to-use **Streamlit UI**
* Automatically calculates **total working time**
* Supports **overnight shifts** (if Out-Time is earlier than In-Time)
* Generates a **professional WhatsApp message format**
* Copy the generated message easily
* Send the message directly using **WhatsApp Web / App**
* Optional **logo support** at the top of the app

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Streamlit**
* **Pillow (PIL)** *(optional, for reliable image/logo loading)*
* **urllib.parse** (for WhatsApp URL encoding)
* **datetime** (for time calculations)

---

## 📁 Project Structure

```bash
Daily Task Report Tool/
│── app.py
│── logo.png
│── README.md
│── requirements.txt   (optional)
```

> If you want better organization, you can store images inside an `assets/` folder:

```bash
Daily Task Report Tool/
│── app.py
│── assets/
│   └── logo.png
│── README.md
```

---

## ⚙️ Installation

### 1. Clone or Download the Project

```bash
git clone <your-repository-link>
cd "Daily Task Report Tool"
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install streamlit pillow
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running, Streamlit will open the app in your browser automatically.

---

## 🧾 How It Works

1. Open the Streamlit app
2. Fill in:

   * Date
   * Name
   * Task Performed
   * In-Time
   * Lunch Break (minutes)
   * Out-Time
   * WhatsApp Number (with country code, without `+`)
3. Click **Generate WhatsApp Message**
4. The app will:

   * Calculate total working time automatically
   * Generate a professional daily task report
   * Show a preview of the message
   * Provide a button to open WhatsApp with the pre-filled message

---

## 📨 Example Output

```text
📅 *Daily Task Report*

Date: 10-04-2026
Name: Zoom
Task Performed:
- Completed Streamlit UI
- Added WhatsApp integration
- Tested report generation

In-Time: 09:00 AM
Lunch Break: 60 minutes
Out-Time: 06:00 PM
Total Time: 8h 0m
```

---

## 📌 Notes

* Enter WhatsApp number in this format:

```text
919876543210
```

* Do **not** use:

  * `+91...`
  * spaces
  * dashes

* The app uses:

```text
https://wa.me/<number>?text=<encoded_message>
```

to open WhatsApp directly.

---

## 🧠 Core Logic

### Total Working Time Formula

```text
Total Time = Out-Time - In-Time - Lunch Break
```

* If **Out-Time < In-Time**, the app assumes an **overnight shift** and adds **1 day** automatically.

---

## 📦 Optional `requirements.txt`

Create a file named `requirements.txt` with:

```txt
streamlit
pillow
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🌟 Future Enhancements

You can improve this project by adding:

* Multiple task input sections
* Download report as **TXT / PDF**
* Save report history
* Export to **Excel / CSV**
* Dark mode / custom UI theme
* Company branding with logo and colors
* Auto-send integration with APIs (advanced)

---

## 👨‍💻 Author

**Gaurav Ghandat**
Built using **Python + Streamlit** for quick and professional daily reporting.

---

## 📜 License

This project is for **learning, academic, and productivity use**.
You may modify and enhance it as needed.
