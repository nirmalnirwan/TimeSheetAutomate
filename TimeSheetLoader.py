from ast import List
import asyncio
import json
from AttendanceRecord import AttendanceRecord, WorkingFromHomeTask
from EmployeeData import EmployeeData
from WorkJob import WorkJob
from itertools import groupby
import datetime as dt  # Use an alias to prevent conflicts
from EnvironmentReader import read_config
from HttpHandler import save_attendance_record

config :EmployeeData

def __init__():
    global config  
    data = read_config()
    config =  EmployeeData(data['supervisorId'], data['cookie'], data['jobDescription'], data['employeeId'], data['startHour'] ,data['saveUrl'])

async def main():
    __init__()

    if input_validate():
        print('Please check input variable...')
        return

    csv_data_list = WorkJob.read_from_csv('workItems.csv')

    if len(csv_data_list) ==0 :
        print('Please check csv content of the file...')
        return

    await group_by_work_date(csv_data_list)
  
def input_validate()->bool:
    res = len(config.employeeId) == 0 or len(config.supervisorId) == 0 or len(config.cookie) == 0  or len(config.jobDescription) == 0 or config.startHour == 0 
    return res

def get_attendance_dateIn(workDate: dt.datetime.date) -> str:
    datetime_with_time = dt.datetime.combine(workDate, dt.datetime.min.time())
    new_date = datetime_with_time + dt.timedelta(hours=config.startHour)
    return new_date.strftime("%Y-%m-%d %H:%M")

def get_attendance_dateOut(workDate: dt.datetime.date ,total_hours :float) -> str:
    datetime_with_time = dt.datetime.combine(workDate, dt.datetime.min.time())
    new_date = datetime_with_time + dt.timedelta(hours=config.startHour) + dt.timedelta(hours=total_hours)
    return new_date.strftime("%Y-%m-%d %H:%M")

async def group_by_work_date(csv_data_list: list[WorkJob]):
    sorted_data = sorted(csv_data_list, key=lambda x: x.work_date)

    grouped_data = groupby(sorted_data, key=lambda x: x.work_date)

    attendances = set_up_attendance_records(grouped_data)

    if len(attendances) == 0:
        print("No record found......")
        return
    
    await save_attendance(attendances)

async def save_attendance(attendances :list[AttendanceRecord]):
    for item in attendances:
        await save_attendance_record(item.AttendanceDateIn, json.dumps(item.to_json()), config.saveUrl, config.cookie)
    
def set_up_attendance_records(grouped_data:any)->list[AttendanceRecord]:
    attendanceRecords =[]
    for work_date, group in grouped_data:
        tasks =[]
        total_hours = 0  
        for item in group:
            total_hours += item.hours  
            task =WorkingFromHomeTask(f"{item.issue_key}-{item.issue_summary}",item.hours , 0)
            tasks.append(task)
        
        attendance =AttendanceRecord(config.supervisorId,get_attendance_dateIn(work_date) ,get_attendance_dateOut(work_date,total_hours),config.employeeId,config.jobDescription,tasks,0)
        attendanceRecords.append(attendance)
    return attendanceRecords


if __name__ == "__main__":
    asyncio.run(main())
