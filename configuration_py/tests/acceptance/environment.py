import os
import shutil

TMP_FOLDER = 'tmp'


def before_scenario(context, scenario):
    if not os.path.exists(TMP_FOLDER):
        os.makedirs(TMP_FOLDER)

    context.TMP_FOLDER = TMP_FOLDER

    os.environ['ENV'] = os.environ['ENVIRONMENT'] = ''


def after_scenario(context, scenario):
    shutil.rmtree(TMP_FOLDER)