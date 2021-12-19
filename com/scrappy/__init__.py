import WebScraper as wbs
from com.scrappy.GeneratePdf import generatePdfFromPictures


def main():
    print("Welcome To Drappy (Drop-Box Scraper)")
    # url = input("Enter the url to be scraped: ")
    # password = input("Enter the password to Access the DropBox: ")
    # download_folder = input("Enter the folder address to store files: ")
    # print(url+" "+password + " " + download_folder)
    wbs.login_and_download("url", " password");
    # generate_pdf_from_pictures();


main()
