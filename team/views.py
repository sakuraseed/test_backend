from requests.auth import HTTPBasicAuth
from asgiref.sync import sync_to_async
from django.http import HttpResponse, JsonResponse
import requests
import json


# Create your views here.

async def get_employees(request):
    json_data = {"Request_id": "e1477272-88d1-4acc-8e03-7008cdedc81e",
                 "ClubId": "59115d1e-9052-11eb-810c-6eae8b56243b",
                 "Method": "GetSpecialistList",
                 "Parameters": {
                     "ServiceId": ""
                 }}
    crm_response = requests.post(url='http://176.192.70.122:90/fitnes_t_nfc_mobile/hs/nfc_mobile/v1',
                         json=json_data,
                         auth=HTTPBasicAuth('FitnessKit', 'vY0xodyg'))
    employees = crm_response.json()["Parameters"]
    response = []
    for employees in employees:
        response.append({
            'id': employees['ID'] if employees['ID'] else "",
            'phone': employees['Phone'] if employees['Phone'] else "",
            'name': employees['Name'] if employees['Name'] else "",
            'last_name': employees['Surname'] if employees['Surname'] else "",
            'image_url': employees['Photo'] if employees['Photo'] else ""
        })

    return JsonResponse(json.dumps(response), safe=False)