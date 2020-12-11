import pandas as pd
import os


class SubjectControl:
    def __init__(self, key_map_path):
        subjects_key_map = pd.read_csv(key_map_path)
        self.subjects_names = []

    def validate_value(self, value):
        return True if value in self.subjects_names else False


class ProjectControl:
    def __init__(self, projects=None):
        self.projects = [proj for proj in projects if os.path.isdir(proj)]
        self.w_project = None

    def set_project(self, project):
        self.w_project = project

    def get_w_project(self):
        return self.w_project
