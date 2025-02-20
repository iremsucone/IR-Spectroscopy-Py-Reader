import cv2
import numpy as np
from scipy.signal import find_peaks

# Wavenumber reference points (calibration points)
REFERENCE_WAVENUMBERS = [4000, 3000, 2000, 1500, 1000, 600]
selected_pixels = []  # Stores user-selected calibration pixel positions

# Global list to store peak information: (pixel position, wavenumber, [functional group possibilities])
peaks_info = []

# Load the IR spectrum image
image = cv2.imread("spectrum.jpg", cv2.IMREAD_GRAYSCALE)  # Update with your image path
clone = image.copy()

# Functional group identification ranges (each tuple: (upper_bound, lower_bound, description))
FUNCTIONAL_GROUPS = [
    (3700, 3584, "O-H stretching (Alcohol, Free)"),
    (3550, 3200, "O-H stretching (Alcohol, Intermolecular Bonded)"),
    (3500, 3400, "N-H stretching (Primary Amine)"),
    (3400, 3300, "N-H stretching (Aliphatic Primary Amine)"),
    (3350, 3310, "N-H stretching (Secondary Amine)"),
    (3300, 2500, "O-H stretching (Carboxylic Acid, Centered on 3000 cm⁻¹)"),
    (3200, 2700, "O-H stretching (Alcohol, Intramolecular Bonded)"),
    (3000, 2800, "N-H stretching (Amine Salt)"),
    (3100, 3000, "C-H stretching (Alkene)"),
    (3000, 2840, "C-H stretching (Alkane)"),
    (2830, 2695, "C-H stretching (Aldehyde, Doublet)"),
    (2600, 2550, "S-H stretching (Thiol)"),
    (2349, 2349, "O=C=O stretching (Carbon Dioxide)"),
    (2275, 2250, "N=C=O stretching (Isocyanate)"),
    (2260, 2222, "CΞN stretching (Nitrile)"),
    (2260, 2190, "CΞC stretching (Alkyne, Disubstituted)"),
    (2175, 2140, "S-CΞN stretching (Thiocyanate)"),
    (2160, 2120, "N=N=N stretching (Azide)"),
    (2145, 2120, "N=C=N stretching (Carbodiimide)"),
    (2140, 2100, "CΞC stretching (Alkyne, Monosubstituted)"),
    (2000, 1650, "C-H bending (Aromatic Compound, Overtone)"),
    (1750, 1700, "C=O stretching (Carboxylic Acid, Dimer)"),
    (1690, 1640, "C=N stretching (Imine / Oxime)"),
    (1670, 1600, "C=C stretching (Alkene, Various)"),
    (1600, 1300, "C=C stretching (Aromatic)"),
    (1550, 1500, "N-O stretching (Nitro Compound)"),
    (1465, 1375, "C-H bending (Alkane, Methyl / Methylene Group)"),
    (1400, 1000, "C-F stretching (Fluoro Compound)"),
    (1250, 1020, "C-N stretching (Amines)"),
    (1050, 1040, "CO-O-CO stretching (Anhydride)"),
    (1000, 650, "C-H bending (Aromatic, Various)"),
    (900, 700, "C-H bending (Benzene Derivatives)"),
]

# Function to adjust wavenumber calibration using peak distances
def adjust_wavenumber_mapping():
    if len(selected_pixels) != len(REFERENCE_WAVENUMBERS):
        print("Error: Not enough calibration points selected.")
        return lambda x: 4000 - (3600 * (x / image.shape[1]))  # Default linear mapping

    # Compute pixel distances between selected calibration points
    pixel_differences = np.diff(selected_pixels)
    wavenumber_differences = np.diff(REFERENCE_WAVENUMBERS)
    # Compute correction factors for each segment
    correction_factors = wavenumber_differences / pixel_differences

    # Create a function that adjusts the mapping for any x position
    def corrected_mapping(x):
        for i in range(len(selected_pixels) - 1):
            if selected_pixels[i] <= x < selected_pixels[i + 1]:
                return REFERENCE_WAVENUMBERS[i] - (selected_pixels[i] - x) * correction_factors[i]
        return 4000 - (3600 * (x / image.shape[1]))  # Default fallback
    return corrected_mapping

# Step 1: Calibration - User selects wavenumber reference points
def select_wavenumber(event, x, y, flags, param):
    global selected_pixels, pixel_to_wavenumber_function
    if event == cv2.EVENT_LBUTTONDOWN and len(selected_pixels) < len(REFERENCE_WAVENUMBERS):
        selected_pixels.append(x)
        print(f"Selected {REFERENCE_WAVENUMBERS[len(selected_pixels) - 1]} cm⁻¹ at pixel {x}")

        # Draw a marker at the selected point
        cv2.circle(image, (x, y), 5, (255, 255, 255), -1)

        # When all calibration points are selected, set up the mapping function
        if len(selected_pixels) == len(REFERENCE_WAVENUMBERS):
            pixel_to_wavenumber_function = adjust_wavenumber_mapping()
            print("Calibration completed. Now click on peaks.")

# Step 2: Identify peaks - On click, determine wavenumber and list all matching functional groups
def identify_peak_on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(selected_pixels) == len(REFERENCE_WAVENUMBERS):
        wavenumber = pixel_to_wavenumber_function(x)
        # Collect all matching functional groups
        matches = [fg[2] for fg in FUNCTIONAL_GROUPS if fg[0] >= wavenumber >= fg[1]]
        if not matches:
            matches = ["Unknown Functional Group"]
        print(f"Clicked Peak: {wavenumber:.1f} cm⁻¹ -> {', '.join(matches)}")
        # Annotate the image with the peak information
        cv2.putText(image, f"{int(wavenumber)} cm⁻1", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        # Store the peak data
        peaks_info.append((x, wavenumber, matches))

# Final summary: Print all peaks and overall functional groups identified
def final_results():
    if not peaks_info:
        print("No peaks were selected.")
        return
    print("\nFinal Results:")
    overall_functions = set()
    for idx, (x, wn, funcs) in enumerate(peaks_info, 1):
        print(f"Peak {idx}: {wn:.1f} cm⁻¹ -> {', '.join(funcs)}")
        overall_functions.update(funcs)
    print("\nOverall possible functional groups identified:")
    print(", ".join(overall_functions))

# Step 3: Start interactive calibration
print("Step 1: Click on 4000, 3000, 2000, 1500, 1000, and 600 cm⁻¹ in order.")
cv2.namedWindow("IR Spectrum")
cv2.setMouseCallback("IR Spectrum", select_wavenumber)

while len(selected_pixels) < len(REFERENCE_WAVENUMBERS):
    cv2.imshow("IR Spectrum", image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'ESC' to exit
        cv2.destroyAllWindows()
        exit()

# Step 4: Click to identify peaks (after calibration is done)
cv2.setMouseCallback("IR Spectrum", identify_peak_on_click)
print("Step 2: Click on peaks to identify wavenumbers and functional groups.")

while True:
    cv2.imshow("IR Spectrum", image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'ESC' to exit
        break

cv2.destroyAllWindows()

# Output the final summary results to the console
final_results()
