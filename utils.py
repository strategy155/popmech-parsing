import os
import requests
import bs4


def create_directory_if_needed(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return None


def produce_path(path,directory):
    return os.path.join(path,directory)


def get_webpage(url):
    _imported_web_page = requests.get(url)
    _imported_web_page.encoding='utf-8'
    return _imported_web_page


def make_soup_with_webpage(input_webpage, webpage_type):
    _imported_web_page_in_soup=bs4.BeautifulSoup(input_webpage.text, webpage_type+'.parser')
    return _imported_web_page_in_soup


def get_list_of_tags_with_specified_atributes(soup, tag_name, spec_dict):
    _all_spec_headers = soup.find_all(name=tag_name, attrs=spec_dict)
    return _all_spec_headers


def get_tags_with_special_attrs(webpage_url,webpage_type,tag_name, spec_dict):
    _req_page = get_webpage(webpage_url)
    _soup = make_soup_with_webpage(_req_page, webpage_type)
    _tags=get_list_of_tags_with_specified_atributes(_soup,tag_name,spec_dict)
    return _tags


def download_file(url,path=''):
    local_filename = produce_path(path, _pm_article_path_template_creation(url))
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def _pm_article_path_template_creation(path):
    _new_path=path.split('/')[-2].replace("-"," ")
    list = _new_path.split(' ')
    list.pop(0)
    return _new_path