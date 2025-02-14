# IR-Spectroscopy-Py-Reader

Current Development Status
🚧 This project is still under modification! 🚧

Missing Features:
Currently, the script does not yet define peak strength (intensity levels).
It also does not display all possible functional groups associated with a given peak.
Upcoming Improvements:
I am working on adding peak intensity calculations to classify peaks as strong, medium, or weak.
A functional group database will be integrated to provide multiple possible functional groups for each detected peak.###

**Infrared Spectroscopy Spectrum Python Reader (4000 cm⁻¹ to 400 cm⁻¹)**  

This Python script processes and identifies peaks in an **Infrared (IR) spectroscopy spectrum image** within the range of **4000 cm⁻¹ to 400 cm⁻¹**. It helps analyze IR spectra by calibrating wave numbers and detecting peaks accurately.  

### **How to Use:**  

1. **Setup:**  
   - Download the folder and **delete** the provided example spectrum.  
   - Replace it with your own spectrum image, ensuring it is named **exactly** as `spectrum.jpg`.  

2. **Running the Script:**  
   - Launch the script.  
   - You will be prompted to **define** key wave numbers (4000, 3000, 2000, 1500, 1000, 600 cm⁻¹) directly on the image.  
   - This step calibrates the distances for accurate peak detection.  

3. **Peak Identification:**  
   - Once calibration is complete, you can begin analyzing and identifying peaks.  

4. **Exit the Program:**  
   - Use **Ctrl + C** to exit the script safely.  

### **License - GNU Affero General Public License v3.0 (AGPL-3.0)**  

This project is licensed under the **GNU AGPL-3.0**, meaning:  
- You are **free to use, modify, and distribute** the software.  
- If you modify and deploy it as a service, you must **also release your modifications under AGPL-3.0**.  
- The full terms can be found in the [LICENSE](LICENSE) file.  

This ensures that all derivative works remain open-source and accessible to the community.
