from papago import translate
from phind import send_prompt
from extractor import extract
from html_translator import local_translate


def write_essay(topic):
    detailed_result = ''

    eng = translate(topic, 'ko','en')
    
    result = send_prompt(eng)
    # sub_topics = extract(result)
    
    # result = translate(result, 'en','ko')
    # result = local_translate(result)
    
    return result.replace('\n','')
    # if len(sub_topics) == 0:
    #     return result

    # for sub_topic in sub_topics:
    #     detailed_result += send_prompt('write an essay about \"'+sub_topic+'\", as a subsection of \"'+topic+'\"')

    # return detailed_result