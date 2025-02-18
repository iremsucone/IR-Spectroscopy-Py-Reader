# **IR-Spectroscopy-Py-Reader** 🔬  

A **Python-based infrared (IR) spectroscopy spectrum reader** that processes spectral data from **4000 cm⁻¹ to 400 cm⁻¹**. This tool helps identify IR peaks by calibrating wave numbers and detecting functional groups from an IR spectrum image, **without internet** !

---

## 🚧 **Current Development Status** 🚧  
This project is still under modification ! It works, but it’s not perfect yet.  

###  **Missing Features:**  
❌ **Peak strength detection** – The script doesn’t yet classify peaks as **strong, medium, or weak**.  
❌ **Full functional group identification** – Right now, at **3300 cm⁻¹**, for example, it might suggest **either** an alcohol **or** an alkyne stretch, but not both at the same time.  

###  **What’s Coming Next?**  
**Peak intensity detection** – Peaks will soon be categorized by strength.  
**Expanded functional group database** – The program will identify **all** possible functional groups for each peak instead of just one.  

---

## 📖 **How to Use**  

### 1️⃣ **Setup**  
- Download the folder.  
- **Delete the provided spectrum example** and replace it with your own spectrum image.  
- Make sure your file is named **exactly** as `spectrum.jpg`. (It has to be jpg, not jpeg, not png etc.) 

### 2️⃣ **Running the Script**  
- Launch the script within the folder using Command Prompt or Windows Terminal.  
- Define key **wave numbers** by clicking on the x-axis on the image:  
   - **4000 cm⁻¹, 3000 cm⁻¹, 2000 cm⁻¹, 1500 cm⁻¹, 1000 cm⁻¹, 600 cm⁻¹**.  
- The program will use these points to **calibrate distances** and improve peak detection accuracy.  

### 3️⃣ **Peak Identification**  
- Click on strong and medium peaks to analyze them - or on the peaks that seem really important.  
- The script will return the **functional group** based on the wavenumber.  

### 4️⃣ **Exit**  
To exit the program, press **Ctrl + C**.  

---

  
