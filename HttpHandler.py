import requests

async def save_attendance_record(workdate,payload,url,cookie):

        headers = {'Cookie': cookie ,'Content-Type': 'application/json'}

        print(f"Work Date:{workdate.split()[0]}\n-------Payload:{payload}")

        try:
            response = requests.post(url, headers=headers, data=payload ,timeout=(5, None))
            
            if response.status_code == 200:
                print("POST request successful!")
            else:
                print("POST request failed with status code:", response.status_code)

        except Exception as e:
            print("An error occurred:", e)


       



