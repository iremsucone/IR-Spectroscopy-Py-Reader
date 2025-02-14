
---

# **IR-Spectroscopy-Py-Reader** 🔬  

A **Python-based infrared (IR) spectroscopy spectrum reader** for analyzing spectral data between **4000 cm⁻¹ and 400 cm⁻¹**. This tool calibrates peak positions and assists in identifying functional groups from an IR spectrum image.  

---

## **🚧 Development Status**
**This project is under active development.** Current version supports peak detection but lacks peak intensity classification and multiple functional group identification.  

### **⚠️ Missing Features:**  
- **Peak Strength Detection** – Does not yet classify peaks as strong, medium, or weak.  
- **Comprehensive Functional Group Identification** – Limited to detecting **one** functional group per peak.  

### **🔄 Upcoming Improvements:**  
- **Peak Intensity Analysis** – Implementing peak classification based on relative strength.  
- **Expanded Functional Group Database** – Support for multiple possible functional groups at a given wavenumber.  

---

## **📖 Usage Guide**  

### **1️⃣ Setup**  
1. Download the repository.  
2. **Remove the provided sample spectrum**.  
3. Add your own **IR spectrum image** and name it **`spectrum.jpg`**.  

### **2️⃣ Running the Script**  
1. Execute the script.  
2. When prompted, **click on the image to define key reference points** at:  
   - **4000 cm⁻¹, 3000 cm⁻¹, 2000 cm⁻¹, 1500 cm⁻¹, 1000 cm⁻¹, 600 cm⁻¹**.  
3. This step calibrates distances for more accurate peak detection.  

### **3️⃣ Peak Identification**  
- Click on peaks to identify them.  
- The program will return the corresponding **functional group** based on wavenumber.  

### **4️⃣ Exit**  
To close the program, press **Ctrl + C**.  

---

## **📜 License**  

**Licensed under GNU Affero General Public License v3.0 (AGPL-3.0).**  
- Free to **use, modify, and distribute** under the same license.  
- If modified and deployed as a service, **must be released under AGPL-3.0**.  
- See the **[LICENSE](LICENSE)** file for details.  

---

