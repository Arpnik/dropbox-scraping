from com.scrappy.GeneratePdf import generatePdfFromPictures
import DropBoxScraper as dbs


def main():
    print("Welcome To Drappy (Drop-Box Scraper)")
    url = input("Enter the url to be scraped: ")
    password = input("Enter the password to Access the DropBox: ")
    # download_folder = input("Enter the folder address to store files: ")
    dbs.loginAndDownload(url, password)
    generatePdfFromPictures()


main()
