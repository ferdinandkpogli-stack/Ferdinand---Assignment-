# Appointment Rescheduling System - Week 3

```mermaid
C4Context
    title System Context - Appointment Rescheduling

    Person(patient, "Patient", "Wants to reschedule appointment")
    System(appointmentSystem, "Appointment System", "Handles rescheduling logic")
    System_Ext(notification, "Notification Service", "Sends confirmation")
    System_Ext(ehr, "EHR System", "Stores patient records")

    Rel(patient, appointmentSystem, "Requests reschedule")
    Rel(appointmentSystem, notification, "Sends AppointmentRescheduled event")
    Rel(appointmentSystem, ehr, "Updates appointment")
