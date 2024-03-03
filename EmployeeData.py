class EmployeeData:
    def __init__(self, supervisor_id: str, cookie: str, job_description: str, employee_id: str,start_hour: float,save_url: str):
        self.supervisorId = supervisor_id
        self.cookie = cookie
        self.jobDescription = job_description
        self.employeeId = employee_id
        self.startHour = start_hour
        self.saveUrl = save_url

    def to_json(self):
        return {
            "supervisorId": self.supervisorId,
            "cookie": self.cookie,
            "jobDescription": self.jobDescription,
            "employeeId": self.employeeId
        }

