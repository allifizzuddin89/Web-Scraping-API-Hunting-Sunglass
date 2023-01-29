import re
import scrapy
import json

# proxy
from creds import API
from scraper_api import ScraperAPIClient
client = ScraperAPIClient(API)

import logging
logger = logging.getLogger('my_logger')
# logging.warning("This is a warning")
logging.basicConfig(filename="logfile.txt", 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filemode='w',
                    level = logging.DEBUG)

class ApiHuntingSpider(scrapy.Spider):
    name = 'api_hunting'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']

    url ='https://www.sunglasshut.com/wcs/resources/plp/11352/byCategoryId/3074457345626651837?isProductNeeded=true&isChanelCategory=false&pageSize=72&orderBy=default&orderBy=default&responseFormat=json&currency=GBP&viewTaskName=CategoryDisplayView&storeId=11352&DM_PersistentCookieCreated=true&pageView=image&catalogId=20603&top=Y&beginIndex=0&currentPage=1&langId=-24&categoryId=3074457345626651837&orderBy=default&currentPage={}'

    headers = {
        "authority": "www.sunglasshut.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "referer": "https://www.sunglasshut.com/uk/mens-sunglasses?currentPage=4",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24"
    }

    cookies = {
        "bm_sz": "F64F145485616122438882F28D109E93~YAAQFKwwF+tjSdKDAQAANSw6LBHUhk6kxfPuV1NxgtOtTdX4AD25l9g021Uh/rJgK1EYQQOUE7mEd4yGglQf9fB11P81xm4LXgfj6/XuW+KTHB5ihVpJrTT8EqmJ5PQMXY52LY3YC+dc2OIYJi+oy5YpZRC77dabVbEFe5KdmO+bOOPuVQ84XTz5wcFa9+JjwlUMt03ygHhXefieISPjQZKydNLSeIJ/kjkpmRf2XPwiTLzTzY9/bWcASkoxX2tVGjow9jr+jt3vJ/4Mkm0rDTz8ufzt3wj7xplG6OEqyCHbSIThmZsHWA==~4471108~3552050",
        "dtCookie": "v_4_srv_-2D10_sn_1053QGJ2TBLHSLOAH7DNEE02MD4R14HN",
        "rxVisitor": "1667189340097RLEFBAF6U517L6F6DDKBQA8HI9BBAEL1",
        "_abck": "A5B7AB86C57E947DC9691AC57C069DF9~0~YAAQFKwwF/VjSdKDAQAA4IM6LAg9pF0dvMRdL1MJbjwsbcZzbdV1azmVIHK94DDCMO1ZR/OD8JPo143+nmeGO+geW53nGcyfzSR7HWX4vAZSxlm3KoCceYOXTGtxF7l9q5u4xYxN10DE6pdH3ghOLVFuExBZEtePKVtyNjUmUjXEPt7RR3bm8uU7dfFxBeQj9g84JPh+A5Ptfj4Yg74SLivcjkKLug25PoUoaIYZ5LPuhkq8uuVg2RwOkzN6IlUt+QF11V7OJT/8SXwhG0ByGog0no8rqleLJ/K1KA05c2zaLYZ4V2TQmyeCQ8nb99NqWvUdmYj5CSqOOfSiCy4dTL8ydteOhX3Ee69a//cCIZiGMZemF7gA9pmWYEdDWkC7I+CjPa3k0khCvjEyOnYT7rhJG4Y5q/nKc9cC+Q==~-1~||-1||~-1",
        "tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit": "google.com/",
        "tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession": "google.com/",
        "tealium_data_session_timeStamp": "1667189344106",
        "userToken": "undefined",
        "TrafficSource_Override": "1",
        "tiktok_click_id": "undefined",
        "AMCVS_125138B3527845350A490D4C%40AdobeOrg": "1",
        "s_cc": "true",
        "CONSENTMGR": "consent:true%7Cts:1667189347234",
        "SGPF": "CT-2",
        "JSESSIONID": "0000kzfQrM5rq8Cv8ZyVvuyrwoZ:1c7qtngmi",
        "WC_PERSISTENT": "UfEVznIPfDUgAjIYTzXzOXdLcTYDGbb1DhIVfx37nuw%3D%3B2022-10-31+04%3A09%3A40.232_1667189380232-520415_0",
        "hasVisitedPLP": "true",
        "recentlyViewedGB": "3074457345618547170",
        "cookiePolicy": "true",
        "tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit": "210318REF",
        "tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession": "210311ORG-210312REF-210313REF-210314REF-210315REF-210316REF-210317REF-210318REF",
        "s_sq": "%5B%5BB%5D%5D",
        "aka-cc": "MY",
        "aka-ct": "KUALALUMPUR",
        "ak_bmsc": "DF719008774AA548E5E0DB244100DB0A~000000000000000000000000000000~YAAQFKwwFxmBSdKDAQAAhrOxLBEvSCqrB5UQzINULMAU+kOl1xAZv0Ub+oBbfwsIF0BOOabRJaTRhiiBsezssqHgpsUoGhzxKZAAYOsaw08qA6xVJp9IWFC8zFBVYBwxZzetLCxNL/wxlLqzAgMStlIw5Z9NNKjiS/lxzducd3yV9aMBWVl5OArSTnxRVjrIPhXqG3lfyV5HOAzfBUxbmFnqhog4/oDAmOYU7wEwNZunI3it6A/Y0WRslmYmvqBbU4QIviCvistHpo4/UOIal6UeNgiZMCyfyqGJZlCBSnOzRCKppVPR7421dfQLh9mDCEoVtLD24wPGG5TOO1vIkuEyG7O6hAZke07+Uvt0W9w04j0Wd6qoQOMi9VnnM6Rf/iVC/Q2SvL4FMb4imgH2pyIuSs8nKZpU3rpJhc1Xgg+DcxQ4uuB2",
        "rxvt": "1667198964354|1667197164354",
        "AMCV_125138B3527845350A490D4C%40AdobeOrg": "-1303530583%7CMCIDTS%7C19297%7CMCMID%7C02914974196327132162193286093214871320%7CMCAID%7CNONE%7CMCOPTOUT-1667204367s%7CNONE%7CvVersion%7C3.3.0",
        "_cs_mk": "0.27051223708603533_1667197174721",
        "utag_main": "v_id:01842c3a876000188108c4349de405077001e06f00bd0$_sn:2$_se:6$_ss:0$_st:1667199000524$vapi_domain:sunglasshut.com$dc_visit:2$ses_id:1667197167361%3Bexp-session$_pn:2%3Bexp-session$dc_event:2%3Bexp-session",
        "bm_mi": "DDB6C1DE488EAFBB0ADB3F999BD7031D~YAAQGawwF/YilhyEAQAABbLFLBEZEaMaSKRCImEr3NlBNCzkoqcBLSwlT2UH1D9kBzzzbVRX6BwIH0cmicQ3Cgg8kpx35xZ0nYpeAc+uHoyxaWmPoxl7V+la8UCFLfj36OSxJLYwi2Y2y33JQInwknv6/sAl7BEy95I19RZazyW7POB2/g52HqRJETOjm1zewmR8BG56USUpRajEUKzRybPemk0qsaK4s8bnce8dRYAsGWkgvbtjJRsl7UiH71IO/xJu3ezJzbzclM1Me3CfQGpSvEaxWQK2Cj72etyGOzJerJyrDXIggLQ+FrJSBBcLe4XK3G8VkeVaSCbz3+FAkc2y~1",
        "TS011f624f": "015966d29297cf2e1f4534b8351164474477a55b5fa0743d3e822e3e8cfa058bb5b1537b8655367e647bc089dfd4bd5009d954cc42c2ed61c9e965c3f0f1af626ab064b638cebd34c520b0b8a975e4a06a7e93d463",
        "dtPC": "-10$398467537_970h1vGIDAAGTOEHHGPOCTKFTUEKTURVCPMMKM-0e0",
        "forterToken": "45c4af1555c44496953cc9cfd6a02f83_1667198467690_40_UAL9_6",
        "sgh-desktop-facet-state-plp": "categoryid:undefined|gender:true|brands:partial|polarized:true|price:true|frame-shape:partial|color:true|face-shape:false|fit:false|materials:false|lens-treatment:false",
        "bm_sv": "BF9746DB1585C1D1DBF40BCEA2EF441B~YAAQGawwFw4jlhyEAQAAqMPFLBEBUYObg4luXIYw+HgVAnhJP4K+uD1Jc1Z/yMKI9Cnxwy2f6vU1bbbOf4ZMCi2ccRIpNg6JWISyj85fsJUPj8KXgxnvnblLrH5BoWiCUKKDTwgG9S5qW3b2anOJt7fwb9WmKRk4ogjSTRRnfXqAg4ZPbforxVLDrTufhhZwhRoMTh+KrUE1B7z+Wo3ZAHa19MQOQyJR2SrgA53LQrjg8t+B7FVZBaC2HIgEBVgkyVWrOrSZ~1"
    }

    # request = Request(
    #     url=url,
    #     method='GET',
    #     dont_filter=True,
    #     cookies=cookies,
    #     headers=headers,
    # )

    def start_requests(self):
        for i in range(0,72):
            req = scrapy.Request(
                client.scrapyGet(url=self.url.format(i)),
                method='GET',
                dont_filter=True,
                cookies=self.cookies,
                headers=self.headers,
                callback=self.parse_api,
            )
            yield req
    
    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)['plpView']['products']['products']['product']
        for count, item in enumerate(data):
            try :
                product = {
                    'Brand' : data[count]['brand'],
                    'Model Name' : data[count]['modelName'],
                    'Frame Color' :data[count]['frameColor'],
                    'Lens Color' : data[count]['lensColor'],
                    'List Price (£)' :data[count]['listPrice'].strip('£'),
                }
                yield product
            except:
                product = {
                    'Brand' : data[count]['brand'],
                    'Model Name' : data[count]['modelName'],
                    'Frame Color' :data[count]['frameColor'],
                    'Lens Color' : data[count]['lensColor'],
                    'List Price (£)' :data[count]['listPrice'].strip('£'),
                    'Out Of Stock' : data[count]['isOutOfStock'],
                }
                yield product