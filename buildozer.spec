[app]

# (str) Title of your application
title = Presidence choix dune nation

# (str) Package name
package.name = presidence

# (str) Package domain (needed for android/ios packaging)
package.domain = org.nicodeme

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

#
# OSX Specific
#
osx.python_version = 3
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Target Android API, should be as high as possible.
# API 34 corresponds to Android 14. API 35 (Android 15) might not be fully supported yet.
android.api = 34

# (int) Minimum API your APK / AAB will support.
# Setting to 30 for Android 11.
android.minapi = 30

# (str) Python branch to use (e.g. "3.9", "master"). Usually defaults to a stable 3.x
python.branch = 3.9

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) Android permissions
android.permissions = INTERNET, VIBRATE, WRITE_EXTERNAL_STORAGE


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
