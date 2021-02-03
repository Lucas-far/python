

from requests import get
from bs4 import BeautifulSoup


def tag_seeker(domain: str = 'https://google.com', tag_name: str = 'title') -> None:
    """
    Return content inside a specified target tag
    :param domain: str (the website route)
    :param tag_name: str (the name between <></> or <> only)
    :return: None

    REQUIREMENTS: pip install requests beautifulsoup4
    STEP 1: the method will get the domain number and convert it to its textual shape, as HTML, due to method (.text)
    STEP 2: an object of the BeautifulSoup class will be created, in order to find the target tag
    STEP 3: an iteration is executed, in order to use method (next_element) to correct the display of the results
    """

    # step 1
    website_html = get(domain).text

    # step 2
    target_tag = BeautifulSoup(website_html, 'html.parser').find_all(tag_name)

    # step 3
    for obj in target_tag:
        print(obj.next_element)

if __name__ == '__main__':
    tag_seeker(domain='https://www.udemy.com/', tag_name='section')
