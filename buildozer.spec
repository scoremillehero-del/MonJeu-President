[app]
# (str) Title of your application
title = Mon Jeu President

# (str) Package name
package.name = monjeupresident

# (str) Package domain (needed for android packaging)
package.domain = org.president

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# J'ai ajouté les versions stables pour éviter l'erreur de "recette"
requirements = python3,kivy==2.3.0,kivymd,pillow

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
# API 34 est nécessaire pour Android 14 et 15
android.api = 34

# (int) Minimum API your APK will support.
# API 30 correspond à Android 11
android.minapi = 30

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use the private storage for data
android.private_storage = True

# (list) The Android archs to build for.
# arm64-v8a est indispensable pour les téléphones récents
android.archs = arm64-v8a, armeabi-v7a

# (bool) skip update of the index
p4a.skip_update = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
