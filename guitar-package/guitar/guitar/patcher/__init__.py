class Patcher:
    def __init__(self, settings_file, urls_file):
        """
        Add patches to Django settings and urls file
        :param settings_file: settings file
        :param urls_file: urls file
        """
        self.settings_file = settings_file
        self.url_file = urls_file

    def patch(self, path_obj):
        """
        Add code to django settings and urls files
        :param path_obj: Object, generated by confugurtor.Configurator
        """
        pass
