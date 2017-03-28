import os


def get_config_folder_path(context, folder):
    return os.path.join(context.TMP_FOLDER, folder)


def create_config_folder(context, folder):
    config_folder_path = get_config_folder_path(context, folder)
    os.makedirs(config_folder_path)
    return config_folder_path
