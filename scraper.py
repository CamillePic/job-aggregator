import requests
from bs4 import BeautifulSoup

def scrape_indeed():
    url = "https://www.indeed.fr/jobs?q=cherche+poste+responsable+recherche+urbanisme&l=Paris&remote=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_list = []
    for job in soup.find_all("div", class_="job_seen_beacon"):
        title = job.find("h2", class_="jobTitle").text if job.find("h2", class_="jobTitle") else "N/A"
        company = job.find("span", class_="companyName").text if job.find("span", class_="companyName") else "N/A"
        location = job.find("div", class_="companyLocation").text if job.find("div", class_="companyLocation") else "N/A"
        job_list.append({"title": title, "company": company, "location": location})
    return job_list
