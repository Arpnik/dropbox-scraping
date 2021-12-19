import DropBoxScraper as dbs
from com.scrappy.GeneratePdf import generatePdfFromPictures
# from com.scrappy.PropertyConfig import initialize


def main():
    print("Welcome To Drappy (Drop-Box Scraper)")
    # initialize()
    # url = input("Enter the url to be scraped: ")
    # password = input("Enter the password to Access the DropBox: ")
    # download_folder = input("Enter the folder address to store files: ")
    # print(url+" "+password + " " + download_folder)
    dbs.loginAndDownload("df", "asd")
    # generatePdfFromPictures()


main()
