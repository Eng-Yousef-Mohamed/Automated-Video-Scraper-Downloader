from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import requests
##########################################################################################    

# Set up Chrome options to speed up the browser initialization and reduce unnecessary features
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for faster execution (no UI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandbox for faster execution
chrome_options.add_argument("--disable-extensions")  # Disable browser extensions

############################################  setup of script ###########################


# URL of the login page
login_url = ""  # Replace with the actual login page URL

# Login credentials (replace with your credentials)
username = input ("Enetr email:").strip()
password = input("Enter password:").strip()
start_page = int (input("start page number :"))
end_pages =int ( input("end page number :")  )



# Set up the driver (make sure you have ChromeDriver or similar installed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options) #to downlaod dependcisse 
# driver = webdriver.Chrome() # i already have it all in my pc 

# Open the login page
driver.get(login_url)

time.sleep(2)
# Find the username and password fields and login button
username_field = driver.find_element(By.XPATH, '//*[@id="email"]')  # Replace with actual field name XPath
password_field = driver.find_element(By.XPATH, '//*[@id="password"]')  # Replace with actual field password XPath
login_button = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/form/button')  # Replace with actual login button XPath

# Enter the login credentials
username_field.send_keys(username)
password_field.send_keys(password)

# Click the login button
login_button.click()

# Wait for the login to complete
time.sleep(5)  

# Now, you can proceed to scrape the video URLs after login
# Base URL of the pages to scrape
base_url = ""  # Replace with the actual base URL

video_urls = []

# Loop through each page
for page_num in range(start_page, end_pages + 1): #13 ~ 105
    url = f"{base_url}{page_num}"

    driver.get(url)

    time.sleep(3)  # Wait for the page to load (adjust if necessary)
    
    # Find the video elements and extract the 'src' URL from the <source> tag
    video_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'video')))
    
    for video_element in video_elements:
        source = video_element.find_element(By.TAG_NAME, 'source')
        video_url = source.get_attribute('src')
        video_urls.append(video_url)



# Save URLs to a text file
with open('video_urls.txt', 'w') as file:
    for video_url in video_urls:
        file.write(video_url + '\n')

print(f"Collected {len(video_urls)} video URLs.")
driver.quit()

# Download the videos using requests
for video_url in video_urls:
    try:
        print(f"Downloading {video_url} ...")
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Extract filename from URL
        filename = video_url.split("/")[-1]
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

