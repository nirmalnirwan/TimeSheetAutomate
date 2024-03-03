class WorkingFromHomeTask:
    def __init__(self, description: str, hours: float, minutes: float):
        self.Description = description
        self.Hours = int(hours)
        self.Minutes = int((float(hours) - self.Hours) * 60)

    def to_json(self):
        return {
            "Description": f"{self.Description}" , 
            "Hours": f"{self.Hours}" ,
            "Minutes": f"{self.Minutes}" ,
        }

class AttendanceRecord:
    def __init__(self, supervisor_id: str, attendance_date_in: str, attendance_date_out: str, employee_id: str, description: str, working_from_home_task_list: list, update_record_id: int):
        self.SupervisorId = supervisor_id
        self.AttendanceDateIn = attendance_date_in
        self.AttendanceDateOut = attendance_date_out
        self.EmployeeId = employee_id
        self.Description = description
        self.WorkingFromHomeTaskList = working_from_home_task_list
        self.UpdateRecordId = update_record_id

    def to_json(self):
        
        return {
            "SupervisorId": f"{self.SupervisorId}" ,
            "AttendanceDateIn": f"{self.AttendanceDateIn}" ,
            "AttendanceDateOut": f"{self.AttendanceDateOut}",
            "EmployeeId": f"{self.EmployeeId}" ,
            "Description": f"{self.Description}" ,
            "WorkingFromHomeTaskList": [task.to_json() for task in self.WorkingFromHomeTaskList],
            "UpdateRecordId": self.UpdateRecordId
        }

    @staticmethod
    def from_json(json_data):
        working_from_home_task_list = [
            WorkingFromHomeTask(task['Description'], task['Hours'], task['Minutes']) 
            for task in json_data['WorkingFromHomeTaskList']
        ]
        return AttendanceRecord(
            json_data['SupervisorId'],
            json_data['AttendanceDateIn'],
            json_data['AttendanceDateOut'],
            json_data['EmployeeId'],
            json_data['Description'],
            working_from_home_task_list,
            json_data['UpdateRecordId']
        )

