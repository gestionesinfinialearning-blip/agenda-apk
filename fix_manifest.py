import re

path = 'android/app/src/main/AndroidManifest.xml'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'SCHEDULE_EXACT_ALARM'
if marker in content:
    print('Ya estaba aplicado')
else:
    permisos = (
        '    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>\n'
        '    <uses-permission android:name="android.permission.USE_EXACT_ALARM"/>\n'
        '    <uses-permission android:name="android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS"/>\n'
    )
    # Insertamos los permisos justo despues de que cierra la etiqueta <manifest ...>
    match = re.search(r'<manifest[^>]*>', content)
    if not match:
        print('ERROR: no se encontro la etiqueta <manifest>')
    else:
        idx = match.end()
        content = content[:idx] + '\n' + permisos + content[idx:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('OK: permisos agregados al manifest')
