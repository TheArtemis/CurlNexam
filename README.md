# CurlNexam
Easly download exams from "passnexam.com". Currently only supports AZ-900
## Usage
Download the repo with:
```bash
git clone https://github.com/TheArtemis/CurlNexam.git
```
Move to the working directory:
```bash
cd CurlNexam
```
First download the pages with:
```bash
python3 AZ-900/download.py
```
Then start the server using:
```bash
python3 AZ-900/start.py
```
or specify a custom port with:
```bash
python3 AZ-900/start.py <port-number>
```

Freely browse the exam pages at:
```bash
http://localhost:1234
```
