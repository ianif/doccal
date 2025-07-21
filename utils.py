# Utility functions for appointment system

def is_appointment_available(appointments, date, time, doctor, patient):
    """
    Check if the appointment slot is available
    
    Args:
        appointments (set): Set of existing appointments
        date (str): Appointment date
        time (str): Appointment time
        doctor (str): Doctor name
        patient (str): Patient identifier
        
    Returns:
        bool: True if appointment is available, False otherwise
    """
    key = (date, time, doctor, patient)
    return key not in appointments

def add_appointment(appointments, date, time, doctor, patient):
    """
    Add a new appointment to the system
    
    Args:
        appointments (set): Set of existing appointments
        date (str): Appointment date
        time (str): Appointment time
        doctor (str): Doctor name
        patient (str): Patient identifier
        
    Returns:
        bool: True if appointment was added successfully, False otherwise
    """
    key = (date, time, doctor, patient)
    if key not in appointments:
        appointments.add(key)
        return True
    return False

def format_response(status, message):
    """
    Format a JSON response
    
    Args:
        status (str): Status message (success or error)
        message (str): Response message
        
    Returns:
        dict: Formatted response dictionary
    """
    return {"status": status, "message": message}