# Web-Scraping-API-Hunting-Sunglass
- Scraping for data by investigating the hidden API
- Applying proxy by ScraperAPI to circumvent the website's ban.
- Scraping framework : Scrapy
- Scraping through API, extracting data from JSON

## Requirement : 
- Scrapy 2.7.1
- Python 3.7 or above
- Any working environment to install the required packages such as conda or pyenv.

## Run
- The working directory is [here](https://github.com/allifizzuddin89/Web-Scraping-API-Hunting-Sunglass/tree/main/sunglass_scraping/sunglass_scraping/spiders)
- Activate the installed working environment, e.g:
```bash  
  conda activate my_env 
```
- Enter the main.py in the working directory, e.g:
```bash  
  cd Web-Scraping-API-Hunting-Sunglass/spiders
```
- Run <scrapy runspider main.py> in the terminal in the working directory
  OR simply run <scrapy crawl main.py>
- Add -O sunglass_list.csv in terminal to produce the csv file e.g. ''
```bash  
  scrapy runspider main.py -O sunglass_list.csv 
```

### Install environment
- Refer [CONDA Environment Installation](https://docs.anaconda.com/anaconda/install/)
 
### HOW-TO
- Clone the repository
```bash  
  git clone https://github.com/allifizzuddin89/Web-Scraping-API-Hunting-Sunglass.git
  ```
- Create working environment (skip if already have any working environment)
```bash
  conda create --name scraping_env -c conda-forge python=3.9.13 scrapy=2.7.1
```
- Activate the working environment
```bash
  conda activate scraping_env
```
- Run the spider, if you already inside working directory, please [runspider main.py], else,
 ```bash
    scrapy runspider Web-Scraping-API-Hunting-Sunglass/sunglass_scraping/sunglass_scraping/spiders/main.py -O sunglass_list.csv
 ```

## Troubleshoot
- Error might happen due to the cookies already expired or request being rejected by the server or the url simply has been changed by the administrator.
  - Please bear in mind, the the web owner might change the web's code dynamically anytime. Therefore this web scraping code might not work anytime in future.
- Solution: 
  1. Refresh the cookies (if any) OR
  2. Using proxy (refer main.py)
  3. Replace with new url
  4. Update the header
  
## DISCLAIMER
- This works only meant for educational, research and proof of work purpose only. 
- I will not responsible for any illegal activities.
- Please respect the robot.txt rules.
- Please don't overload the website with too much parallel frequent request.
- Every action is on your own responsibilities.


