### Being tired of logging into the website every day and checking whether the status of my application has changed, I wrote a program that will send a notification to my Macbook when the status of the application has changed.

## Running the Program
**1. Clone the Repository:**
-  Clone or download the repository containing statusScraper.py, run_scraper.sh, and notify.scpt to your local machine.

**2. Set Up Environment (if applicable):**
- Ensure Python 3.x is installed on your system.
- If using a virtual environment, create and activate it:
```
cd /path/to/checkStatus/
python3 -m venv myenv
source myenv/bin/activate
```
**3. Install Dependencies:**
-  Install required Python packages:
```
pip install requests beautifulsoup4
```
**4. Configure Script:**
  - Edit statusScraper.py to update login_url, payload (with your credentials, make sure the payload keys are the same as keys on the website you are logging in to), and secured_page_url as needed.

**5. Run the Scraper:**
  - Execute run_scraper.sh in your terminal:
```
cd /path/to/checkStatus/
./run_scraper.sh
```

## Setting Up Automatic Notifications with cron (macOS)
You can schedule the run_scraper.sh script to run at regular intervals using cron to receive automatic notifications.

**1. Edit crontab:**
  - Open your crontab for editing:
```
crontab -e
```
  - Add the following lines to schedule the script:
    - To run every 2 hours (at the top of every hour):
```
0 */2 * * * /bin/bash /path/to/checkStatus/run_scraper.sh >> /path/to/checkStatus/cron.log 2>&1
```
**2. Save and exit crontab:**
  - Save the crontab configuration and exit the editor.

### Follow the steps above to clone the repository, set up the environment, install dependencies, configure the script, and then run run_scraper.sh manually to ensure everything works as expected. Once validated, set up automatic notifications using cron as described.

## Program Functionality
The statusScraper.py script automates website login, retrieves status information, and triggers macOS notifications when status changes are detected.

## Notes
- Ensure all file paths (statusScraper.py, run_scraper.sh, notify.scpt, and previous_status.txt) are correctly configured according to your local environment.
- Adjust cron scheduling (*/2 * * * * for every 2 minutes or 0 */2 * * * for every 2 hours) based on your notification frequency preference.
