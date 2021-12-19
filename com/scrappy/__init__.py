import web_scraper as wbs
from com.scrappy.generate_pdf import generate_pdf_from_pictures


def main():
    print("Welcome To Drappy (Drop-Box Scraper)")
    # url = input("Enter the url to be scraped: ")
    # password = input("Enter the password to Access the DropBox: ")
    # download_folder = input("Enter the folder address to store files: ")
    # print(url+" "+password + " " + download_folder)
    # wbs.login_and_download("url", " password");
    generate_pdf_from_pictures();


main()
