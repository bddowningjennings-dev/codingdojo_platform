
class Patient(object,):
  patientId = 0
  def __init__(self, name, allergies, bed = None,):
    Patient.patientId += 1
    self. name = name.upper()
    self.allergies = allergies
    self.bed = bed
    self.id = Patient.patientId

class Hospital(object,):
  def __init__(self, name, capacity):
    self.beds = []
    for i in range(0, capacity):
      self.beds.append(i)
    self.name = name.upper()
    self.capacity = capacity
    self.patients = []
  def Admit(self, patient,):
    if len(self.patients) >= self.capacity:
      print "Sorry, the hospital is full."
    else:
      self.patients.append(patient)
      patient.bed = self.beds[0]
      self.beds.remove(patient.bed)
      print patient.name, "has been assigned to bed", patient.bed
    return self
  def Discharge(self, patient,):
    if patient.bed == None:
      print "Patient not currently admitted to hospital"
    else:
      self.patients.remove(patient)
      self.beds.append(patient.bed)
      print patient.name, "has been dishcarged, bed", patient.bed, "is now free."
      patient.bed = None
    return self

patient_1 = Patient('Chris butts', 'peanuts')
patient_2 = Patient('Philis butts', '')

hospital_1 = Hospital('Oak pines', 1)

hospital_1.Admit(patient_1)
hospital_1.Admit(patient_2)


hospital_1.Discharge(patient_1)
