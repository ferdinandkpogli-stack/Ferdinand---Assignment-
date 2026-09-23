def reschedule_appointment(original, new, hours_before):
    late_flag = False
    if hours_before < 24:
        late_flag = True
    
    event = "AppointmentRescheduled"
    
    # Emit to Notification Service
    print(f"Event: {event} sent to Notification Service")
    print(f"Original: {original} -> New: {new}")
    
    # Confirmation
    if late_flag:
        message = f"Confirmed! Rescheduled to {new} with LATE-CHANGE flag applied."
    else:
        message = f"Confirmed! Rescheduled to {new}"
    
    return message

# Test with your assignment dates
result = reschedule_appointment(
    "2026-10-15T10:00:00Z", 
    "2026-10-16T14:00:00Z", 
    20  # 20 hours before = less than 24 hours
)
print(result)
