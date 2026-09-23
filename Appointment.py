from datetime import datetime, timezone
from dataclasses import dataclass

@dataclass
class AppointmentRescheduledEvent:
    event_type: str = "AppointmentRescheduled"
    original_time: str = ""
    new_time: str = ""
    late_change_flag: bool = False

    def emit_to_notification_service(self):
        print(f"Event Emitted to Notification Service: {self.event_type}")
        print(f"Original: {self.original_time} -> New: {self.new_time}")
        print(f"Late Change: {self.late_change_flag}")
        return self

class AppointmentSystem:
    def reschedule_appointment(self, original_time_str, new_time_str, request_time_str=None):
        """
        Reschedules appointment within 24 hour window
        """
        original_time = datetime.fromisoformat(original_time_str.replace("Z", "+00:00"))
        
        if request_time_str:
            request_time = datetime.fromisoformat(request_time_str.replace("Z", "+00:00"))
        else:
            request_time = datetime.now(timezone.utc)
        
        # Check if reschedule is less than 24 hours before original time
        time_diff = original_time - request_time
        hours_diff = time_diff.total_seconds() / 3600
        
        late_change_flag = hours_diff < 24

        # Create and emit event
        event = AppointmentRescheduledEvent(
            original_time=original_time_str,
            new_time=new_time_str,
            late_change_flag=late_change_flag
        )
        event.emit_to_notification_service()

        # Display confirmation
        confirmation = f"Appointment rescheduled to {new_time_str}. Late-change flag: {late_change_flag}"
        print(confirmation)
        
        return {
            "original_time": original_time_str,
            "new_time": new_time_str,
            "late_change_flag": late_change_flag,
            "confirmation": confirmation
        }

# Example usage matching your Gherkin
if __name__ == "__main__":
    system = AppointmentSystem()
    system.reschedule_appointment(
        original_time_str="2026-10-15T10:00:00Z",
        new_time_str="2026-10-16T14:00:00Z",
        request_time_str="2026-10-14T12:00:00Z"  # Less than 24h before
    )
