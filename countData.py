import xml.etree.ElementTree as ET
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

# create element tree object
tree = ET.parse('export.xml') 
# for every health record, extract the attributes
root = tree.getroot()

record_elements = list(root.iter('Record'))
print(f"Found {len(record_elements)} <Record> elements.")

correlation_elements = list(root.iter('Correlation'))
print(f"Found {len(correlation_elements)} <Correlation> elements.")

workout_elements = list(root.iter('Workout'))
print(f"Found {len(workout_elements)} <Workout> elements.")

activity_summary_elements = list(root.iter('ActivitySummary'))
print(f"Found {len(activity_summary_elements)} <ActivitySummary> elements.")

clinical_record_elements = list(root.iter('ClinicalRecord'))
print(f"Found {len(clinical_record_elements)} <ClinicalRecord> elements.")

audiogram_elements = list(root.iter('Audiogram'))
print(f"Found {len(audiogram_elements)} <Audiogram> elements.")

vision_prescription_elements = list(root.iter('VisionPrescription'))
print(f"Found {len(vision_prescription_elements)} <VisionPrescription> elements.")

