from bs4 import BeautifulSoup
from .HTMLParser import *


def createXpath(tags):
    xpath = ['//*[@' + key + "='" + ' '.join(value) + "']" if type(value) is list else
             '//*[@' + key + "='" + value + "']" for key, value in tags.attrs.items()]
    # [print(path) for path in xpath]
    return xpath


class ParseDOM:

    def give_locator_all_inputBoxes(self, source):
        all_paths = []
        try:
            doc = BeautifulSoup(source, "html.parser")
            tag = doc.find_all('input')
            for tags in tag:
                if 'hidden' not in str(tags).lower():
                    print(f'***** Html Tag *****')
                    # identifiers = ['text','password']
                    print(f'{tags}')
                    html_tag_identified = [html_tags for html_tags in HtmlParser().type_input_box() if
                                           html_tags in str(tags).lower()]
                    if 'password' in str(html_tag_identified[0]).lower():
                        print(f'***** Xpath Identified for Password Field *****')
                        xpath = createXpath(tags=tags)
                        all_paths.append(xpath)
                    elif 'text' in str(html_tag_identified[0]).lower():
                        print(f'***** Xpath Identified for Text Field *****')
                        xpath = createXpath(tags=tags)
                        all_paths.append(xpath)
                    elif 'submit' in str(html_tag_identified[0]).lower():
                        print(f'***** Xpath Identified for Submit Form *****')
                        xpath = createXpath(tags=tags)
                        all_paths.append(xpath)

            return all_paths
        except:
            raise Exception('ERROR - not able to generate the xpath!')
