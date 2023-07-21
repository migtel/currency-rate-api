import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_soup():
    disable_warnings(InsecureRequestWarning)
    url = "https://www.bcv.org.ve/"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


@app.get("/")
async def get_all():
    soup = await get_soup()
    dolar = float(
        soup.find("div", {"id": "dolar"})
        .text.strip()
        .replace(",", ".")
        .replace("USD \n ", "")
    )
    euro = float(
        soup.find("div", {"id": "euro"})
        .text.strip()
        .replace(",", ".")
        .replace("EUR  \n ", "")
    )
    yuan = float(
        soup.find("div", {"id": "yuan"})
        .text.strip()
        .replace(",", ".")
        .replace("CNY  \n ", "")
    )
    lira = float(
        soup.find("div", {"id": "lira"})
        .text.strip()
        .replace(",", ".")
        .replace("TRY \n ", "")
    )
    rublo = float(
        soup.find("div", {"id": "rublo"})
        .text.strip()
        .replace(",", ".")
        .replace("RUB \n ", "")
    )
    return {
        "usd": dolar,
        "eur": euro,
        "cny": yuan,
        "try": lira,
        "rub": rublo
    }


@app.get("/usd")
async def get_usd():
    soup = await get_soup()
    dolar = float(
        soup.find("div", {"id": "dolar"})
        .text.strip()
        .replace(",", ".")
        .replace("USD \n ", "")
    )
    return dolar


@app.get("/eur")
async def get_eur():
    soup = await get_soup()
    euro = float(
        soup.find("div", {"id": "euro"})
        .text.strip()
        .replace(",", ".")
        .replace("EUR  \n ", "")
    )
    return euro


@app.get("/cny")
async def get_cny():
    soup = await get_soup()
    yuan = float(
        soup.find("div", {"id": "yuan"})
        .text.strip()
        .replace(",", ".")
        .replace("CNY  \n ", "")
    )
    return yuan


@app.get("/try")
async def get_try():
    soup = await get_soup()
    lira = float(
        soup.find("div", {"id": "lira"})
        .text.strip()
        .replace(",", ".")
        .replace("TRY \n ", "")
    )
    return lira


@app.get("/rub")
async def get_rub():
    soup = await get_soup()
    rublo = float(
        soup.find("div", {"id": "rublo"})
        .text.strip()
        .replace(",", ".")
        .replace("RUB \n ", "")
    )
    return rublo
