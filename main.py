import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import Optional

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/dolar")
async def get_dolar(dolar_type: Optional[str] = None):
    disable_warnings(InsecureRequestWarning)
    url = 'https://www.bcv.org.ve/'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    dolar = float(soup.find('div', {'id': 'dolar'}).text.strip().replace(',', '.').replace("USD \n ", ""))
    return dolar
