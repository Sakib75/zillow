from http.cookies import SimpleCookie
from urllib.parse import urlparse,parse_qs,urlencode
import json
URL = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-80.44818281103514%2C%22east%22%3A-80.04649518896483%2C%22south%22%3A25.643674177628945%2C%22north%22%3A25.9015227616211%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isPreMarketForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketPreForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22,%22total%22]}&requestId=4"

def cookie_parser():
    cookie_string = "zguid=23|%24a816aae5-68fe-4e37-b054-74055ef955ed; _ga=GA1.2.379655208.1597015716; _gid=GA1.2.947044510.1597015716; _pxvid=0dc37e7d-da98-11ea-8d42-0242ac120004; zjs_user_id=null; zjs_anonymous_id=%22a816aae5-68fe-4e37-b054-74055ef955ed%22; _gcl_au=1.1.2132203277.1597015718; KruxPixel=true; _pin_unauth=dWlkPU5UUTVNV1prTWpZdFpqTXdZUzAwTXpNd0xUZzBZekV0TkRjMFl6UTVObUUzTm1RNQ; KruxAddition=true; ki_r=; ki_s=; zgsession=1|e9ea60c7-53be-49ce-b9e5-cbbc332dd173; JSESSIONID=488EC86B01F2EDCFF8D748637B113557; DoubleClickSession=true; GASession=true; _derived_epik=dj0yJnU9dW91VHBRNHpJZDltSTZYNC1JMHAwWDNoVl9xSFVhN24mbj12RWRXTm41NXNzQ25ROTRobklmZlJ3Jm09MSZ0PUFBQUFBRjh4VVE0JnJtPTEmcnQ9QUFBQUFGOHhVUTQ; _px3=111c47ff6d1ce738f8a590a4a06fa4449a4fc32d3864264c150d2883511a8465:x+P3s6e2TjvTV5mdhZgrh8jBL4mysXEqwL6Z0PiU4idaIFFzwkUsgvKE8tKKjkNTx8V+/c2hjPjj3hbExPsK+A==:1000:OJVD5TOZDtJWUXCuS6F92SziTzmwUyhSULk/E9Z++ZZEEA2snjPkdrstlBOATe1ypDxT2DMYfEa2AVxOzeeHRRYN75YPC/Gx5cBPD5JQ9a4lnmvaAm9ZfytWdePphJ17d0C8qThNSZmvEMNORkQnNsINPPlLOuwx0n3yiads8pc=; AWSALB=NN9Pgkin0l5p86mJZ1NhSM1hLbBl+melTaktflh6ST9nLnUPjbE08RBpA0xDWn96QJ+1AZqdh3Bp1I6PQJNs/GqPpLCSdijAuBpg7Jmd+sJta6qO6dOTdDCrT7N3; AWSALBCORS=NN9Pgkin0l5p86mJZ1NhSM1hLbBl+melTaktflh6ST9nLnUPjbE08RBpA0xDWn96QJ+1AZqdh3Bp1I6PQJNs/GqPpLCSdijAuBpg7Jmd+sJta6qO6dOTdDCrT7N3; search=6|1599660214752%7Crect%3D25.9015227616211%252C-80.04649518896483%252C25.643674177628945%252C-80.44818281103514%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D0%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0912700%09%09%09%09%09%09; _uetsid=a640155bdd6917c515aaec157651d3af; _uetvid=e7a9c31a85ad4ab883aa64cf73e7ce1d; ki_t=1597015751171%3B1597067552710%3B1597068219042%3B2%3B34; _gat=1"
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies = {}

    for key,morsel in cookie.items():
        cookies[key] = morsel.value
    print(cookies)


def parse_new_url(url,page_number):
    url_parse = urlparse(url)
    query_string = parse_qs(url_parse.query)

    search_query_state = json.loads(query_string.get('searchQueryState')[0])

    search_query_state['pagination'] = {"currentPage": page_number}
  

    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string,doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url

parse_new_url(URL,3)