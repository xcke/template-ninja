import csv
from jinja2 import Environment, PackageLoader, FileSystemLoader
from main import logger
import datetime
import pandas as pd

def two_digit(number):
    if 0 <= number < 10:
        return f"0{number}"
    else:
        return number

def load_csv(configfile):
    """Loads the element from the CSV file and returns as dict """
    results = []
    try:
        df = pd.read_csv(configfile, sep=';', encoding='utf-8')
        df['index'] = range(1, len(df) + 1)
        my_dic = df.to_dict(orient='records')
        return my_dic
    except Exception as e:
        logger.info("There was an issue with loading {}".format(configfile))
        logger.debug(f"Exception was: {e}")

def load_excel(configfile):
    """Loads the element from the CSV file and returns as dict """
    results = []
    try:
        df = pd.read_excel(configfile)
        # create index
        df['index'] = range(1, len(df) + 1)
        my_dic = df.to_dict(orient='records')
        return my_dic
    except Exception as e:
        logger.info("There was an issue with loading {}".format(configfile))
        logger.debug(f"Exception was: {e}")

def load_template(directory, template_name):
    """ Will load the template object from a Directory """
    jinja2_env = Environment(loader=FileSystemLoader(directory))
    jinja2_env.filters['two_digit'] = two_digit
    template = jinja2_env.get_template(template_name)
    return template

def datetimenow():
    """
    Function for datetime
    :return:
    """
    now = datetime.datetime.now()
    return str(now.strftime("%Y%m%d%H%M"))