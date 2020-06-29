from dynamicScrapper import Page
import bs4 as bs

def scrape_job_page(url):
    page = Page(url)
    soup = bs.BeautifulSoup(page.html, 'html.parser')


    cardDescription = soup.find("ul", {"class": "job-posting-brief"}) #<ul>
    cardKeys = []
    cardValues = []
    for div in cardDescription.find_all("span", {"class": "wb-inv"}):
        cardKeys.append(div.text)
        div.decompose()

    for element in cardDescription.find_all("li"):
        cardValues.append(element.text.replace("\t",'').replace("\n","").lstrip())

    print(cardValues)

    advertisedUntil = soup.find(property="validThrough").text.strip() #<p> tag

    try:
        externalLink = soup.find(id="externalJobLink").get("href")
    except:
        print("No external link, hosted on JobBank")
        language = soup.find("div", {"class": "job-posting-detail-requirements"}).p.text
        educationRequirements = soup.find(property="educationRequirements").text  # <p>
        experienceRequirements = soup.find(property="description experienceRequirements").text  # <p>
        skills = soup.find(property="skills")  # <div> # TODO Format this
        employmentGroup = soup.find(id="employmentGroup").p.text  # <div>
        #howtoapply = soup.find(id="howtoapply")  # <div>. This doesn't work because we have to click on a button







