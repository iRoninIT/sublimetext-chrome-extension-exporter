# Export Chrome Extension for Sublime Text

This Sublime Text plugin allows you to export your Chrome Extension files from the current project into a ZIP file. It excludes specified directories and file types, which you can customize via the settings. The resulting ZIP file will include the version number from the `manifest.json` file and a timestamp in its filename.

## Installation

You can install this plugin via [Package Control](https://packagecontrol.io/installation).

1. Open "Package Control: Install Package" from the Command Palette (`Ctrl+Shift+P`).
2. Search for "Export Chrome Extension" and hit Enter to install.

If you prefer a manual installation, clone this repository into your Sublime Text's Packages directory.

## Usage

Once the plugin is installed, you can use it by running the "Export Chrome Extension" command from the Command Palette (`Ctrl+Shift+P`). The plugin will create a ZIP file in the root directory of your current project.

## Configuration

You can customize the directories and file types that are excluded when creating the ZIP file. To do this, open the `ExportChromeExtension.sublime-settings` file and modify the `excluded_dirs` and `excluded_extensions` settings.

Here is an example of what the settings file might look like:

```json
{
    "excluded_dirs": [".git"],
    "excluded_extensions": [".zip"]
}
```

## Support

If you encounter any issues or have any questions about this plugin, please create an issue on the [GitHub repository](https://github.com/iRoninIT/sublimetext-chrome-extension-exporter).

## Author

[iRonin.IT - Software Development Agency](https://www.ironin.it)

