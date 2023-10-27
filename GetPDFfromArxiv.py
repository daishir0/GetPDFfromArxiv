import requests
from lxml import html
import os
import sys
import time
import re
import PyPDF2
from io import BytesIO

def download_pdfs(keyword):
    # Ensure the pdfs directory exists
    if not os.path.exists('./pdfs'):
        os.makedirs('./pdfs')

    # Form the search URL
    search_url = f"https://arxiv.org/search/?query=%22{keyword.replace(' ', '+')}%22&searchtype=abstract&abstracts=show&order=-announced_date_first&size=200"
    print(f"Accessing URL: {search_url}")
    response = requests.get(search_url)
    response.raise_for_status()  # Check if the request was successful

    # Parse the HTML
    tree = html.fromstring(response.content)

    # Get the number of results
    num_results = len(tree.xpath('//ol[@class="breathe-horizontal"]/li'))

    # Download each PDF
    for i in range(1, num_results + 1):
        pdf_xpath = f'/html/body/main/div[2]/ol/li[{i}]/div/p/span/a[1]'
        title_xpath = f'/html/body/main/div[2]/ol/li[{i}]/p[1]'
        
        pdf_link_element = tree.xpath(pdf_xpath)
        title_element = tree.xpath(title_xpath)
        
        if pdf_link_element and title_element:
            pdf_url = pdf_link_element[0].attrib['href']
            title_text = title_element[0].text_content()
            # Remove or replace invalid characters from the title
            pdf_title = re.sub(r'[<>:"/\\|?*]', '', title_text.strip().replace(' ', '_'))
            
            # Check if the PDF is already downloaded
            if os.path.exists(f"./pdfs/{pdf_title}.pdf") or os.path.exists(f"./pdfs/NG_{pdf_title}.pdf"):
                print(f"Skipping already downloaded PDF: {pdf_title}.pdf")
                continue

            # Ensure that the URL starts with 'https://arxiv.org'
            if not pdf_url.startswith('https://arxiv.org'):
                pdf_url = f"https://arxiv.org{pdf_url}"

            # Skip if the URL does not end with '.pdf'
            if not pdf_url.endswith('.pdf'):
                print(f"Skipping non-PDF URL: {pdf_url}")
                continue

            # Retry logic
            for retry in range(5):  # Retry up to 5 times
                try:
                    print(f"Downloading PDF from URL: {pdf_url}")
                    pdf_response = requests.get(pdf_url)
                    pdf_response.raise_for_status()  # Check if the request was successful

                    # Check if the keyword is present in the PDF text
                    pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_response.content))
                    pdf_text = ' '.join([pdf_reader.pages[page_num].extract_text() for page_num in range(len(pdf_reader.pages))])
                    if keyword.lower() not in pdf_text.lower():
                        pdf_title = f"NG_{pdf_title}"

                    # Save the PDF
                    pdf_path = f"./pdfs/{pdf_title}.pdf"
                    with open(pdf_path, 'wb') as pdf_file:
                        pdf_file.write(pdf_response.content)
                    print(f"Downloaded {pdf_title}.pdf")
                    break  # Break out of the retry loop on success
                except (requests.exceptions.RequestException, PyPDF2.errors.PdfReadError) as e:
                    print(f"Failed to download {pdf_title}.pdf: {e}")
                    if retry < 4:
                        print(f"Retrying in 1 minute... (retry {retry + 1}/5)")
                        time.sleep(60)  # Sleep for 1 minute before retrying
                    else:
                        print(f"Giving up on {pdf_title}.pdf after 5 attempts.")
        else:
            print(f"PDF link or title not found for result {i}")

        # Sleep for a short duration to avoid overwhelming the server
        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python GetPDFfromArxiv.py <search keyword>")
        sys.exit(1)
    keyword = sys.argv[1]
    download_pdfs(keyword)
