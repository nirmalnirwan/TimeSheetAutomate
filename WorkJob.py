import csv
import datetime as dt  # Use an alias to prevent conflicts

class WorkJob:
    def __init__(self, issue_key: str, issue_summary: str, hours: float, work_date: str, user_account_id: str, full_name: str):
        self._issue_key = issue_key
        self._issue_summary = issue_summary
        self._hours = hours
        self._work_date = dt.datetime.strptime(work_date, '%m/%d/%Y').date()
        self._user_account_id = user_account_id
        self._full_name = full_name
        
    @property
    def issue_key(self) -> str:
        return self._issue_key

    @property
    def issue_summary(self) -> str:
        return self._issue_summary

    @property
    def hours(self) -> float:
        return self._hours

    @property
    def work_date(self) -> dt.datetime.date:
        return self._work_date

    @property
    def user_account_id(self) -> str:
        return self._user_account_id

    @property
    def full_name(self) -> str:
        return self._full_name

    # Setter methods if needed (not used in this example)

    def __str__(self):
        return f"Issue Key: {self.issue_key}, Issue Summary: {self.issue_summary}, Hours: {self.hours}, Work Date: {self.work_date}, User Account ID: {self.user_account_id}, Full Name: {self.full_name}"

    @classmethod
    def read_from_csv(cls, file_path):
        data_list = []
        with open(file_path, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data_list.append(cls(
                    row['ï»¿Issue Key'],
                    row['Issue summary'],
                    float(row['Hours']),
                    row['Work date'],
                    (row['User Account ID']),
                    row['Full name']
                ))
        return data_list