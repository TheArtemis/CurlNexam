import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

NUM_PAGES = 39
PAGES_FOLDER = "AZ-900/pages"
AZ_900_URL = "https://www.passnexam.com/microsoft/az-900"

def download_pages():
    os.makedirs(PAGES_FOLDER, exist_ok=True)

    def download_page(page_num):
        url = f"{AZ_900_URL}/{page_num}"
        response = subprocess.run(["curl", url], capture_output=True, text=True)
        if response.returncode == 0:
            print(f"Downloaded page {page_num} from {url}")
            with open(f"{PAGES_FOLDER}/{page_num}.html", "w") as file:
                file.write(response.stdout)
        else:
            print(f"Error downloading page {page_num}: {response.stderr}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_page, range(1, NUM_PAGES))

    print("All pages have been downloaded successfully.")
    
    with open(os.path.join(f"{PAGES_FOLDER}", "index.html"), "w") as index_file:
        index_file.write("""
        <html>
        <head>
            <title>AZ-900</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                }
                .grid-container {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
                    gap: 10px;
                    padding: 10px;
                }
                .grid-item {
                    background-color: white;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    text-align: center;
                    padding: 10px;
                    transition: transform 0.2s;
                }
                .grid-item:hover {
                    transform: scale(1.05);
                    border-color: #007BFF;
                }
                a {
                    text-decoration: none;
                    color: #007BFF;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Page Index</h1>
            <div class="grid-container">
        """)
        for i in range(1, NUM_PAGES):
            index_file.write(f'<div class="grid-item"><a href="{i}.html">{i}</a></div>\n')
        index_file.write("""
            </div>
        </body>
        </html>
        """)

    print("Index file created successfully.")

download_pages()