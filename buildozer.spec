[app]
title = Mon Jeu President
package.name = monjeupresident
package.domain = org.president
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Correction : on simplifie pour éviter l'erreur de "recipe"
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Correction : on passe à l'API 33 pour éviter l'erreur "Aidl not found"
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0

android.private_storage = True
# On garde uniquement arm64 pour que ce soit plus rapide et stable
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
