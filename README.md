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
To see the currently supported exams you can type:
```bash
ls -d */ | sed 's#/##'
```
If necessary use the following command to make the script executable:
```bash
chmod +x start.sh
```
When opening for the first time an exam run the command:
```bash
./start.sh <exam_name> -d
```
**Note**: This command also starts the server.

Any other time you need to open an already initialized exam you can use the following command, specifying a port number if desired:
```bash
./start.sh <exam_name> -p <port_number>
```
Freely browse the exam pages at the following address:
```bash
http://localhost:<port_number>
```
The default port number is ```1234```.

**Happy Studying!**
