"""
Plugin Name: Chrome Extension Exporter
Description: This Sublime Text plugin exports Chrome Extension files from the current project as ZIP, excluding the .git directory and .zip files. Used for quick local distribution.
Version: 1.0.0
Author: iRonin.IT (https://www.ironin.it)
"""

import os
import json
import zipfile
from datetime import datetime
import sublime
import sublime_plugin

class ChromeExtensionExporterCommand(sublime_plugin.TextCommand):
    command_name = "Chrome Extension Exporter"

    def run(self, edit):
        # Get the current file path.
        file_path = self.view.file_name()

        if file_path is None:
            sublime.message_dialog("No file open.")
            return

        # Get the current project path.
        project_path = os.path.dirname(file_path)

        # Check if manifest.json exists in the project root.
        manifest_path = os.path.join(project_path, "manifest.json")
        if not os.path.isfile(manifest_path):
            sublime.message_dialog("manifest.json file not found in project root.")
            return

        # Read the manifest.json file and extract the version.
        with open(manifest_path, 'r') as manifest_file:
            manifest = json.load(manifest_file)
            version = manifest.get('version', '')

        # Get the current timestamp.
        timestamp = datetime.now().strftime('%Y%m%d%H%M')

        # Output zip file will be in the same directory as the project, with the project's name, version and timestamp.
        output_filename = os.path.join(project_path, os.path.basename(project_path) + "-" + version + "-" + timestamp + ".zip")

        # Load user settings for exclusion patterns.
        settings = sublime.load_settings('ExportChromeExtension.sublime-settings')
        excluded_dirs = settings.get('excluded_dirs', ['.git'])
        excluded_extensions = settings.get('excluded_extensions', ['.zip'])

        # Open the zip file in write mode.
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(project_path):
                # Exclude directories based on user settings.
                dirs[:] = [d for d in dirs if d not in excluded_dirs and not any(f.endswith(tuple(excluded_extensions)) for f in os.listdir(os.path.join(root, d)))]

                # Write each file to the zip file, excluding files based on user settings.
                for file in files:
                    if not file.endswith(tuple(excluded_extensions)):
                        full_path = os.path.join(root, file)
                        relative_path = os.path.relpath(full_path, project_path)
                        zf.write(full_path, relative_path)

        sublime.message_dialog("Chrome Extension exported successfully.")
