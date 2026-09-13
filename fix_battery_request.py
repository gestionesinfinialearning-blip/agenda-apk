import re

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'PEDIR_BATERIA_AUTO'
if marker in content:
    print('Ya estaba aplicado')
else:
    patch = """
<script>
// PEDIR_BATERIA_AUTO
(function(){
  function pedirPermisos(){
    try{
      var DKMA = window.Capacitor && Capacitor.Plugins && Capacitor.Plugins.DontKillMyApp;
      if(!DKMA){ if(window.debugLog) window.debugLog('DontKillMyApp no disponible'); return; }
      DKMA.requestKeepAppActive()
        .then(function(r){ if(window.debugLog) window.debugLog('Bateria: pedido=' + JSON.stringify(r)); })
        .catch(function(e){ if(window.debugLog) window.debugLog('Bateria ERROR: ' + e.message); });
      DKMA.requestAutoStart()
        .then(function(r){ if(window.debugLog) window.debugLog('AutoStart: pedido=' + JSON.stringify(r)); })
        .catch(function(e){ if(window.debugLog) window.debugLog('AutoStart ERROR: ' + e.message); });
    }catch(e){
      if(window.debugLog) window.debugLog('ERROR general permisos: ' + e.message);
    }
  }
  setTimeout(pedirPermisos, 2500);
})();
</script>
"""
    idx = content.rfind('</body>')
    if idx == -1:
        content = content + patch
    else:
        content = content[:idx] + patch + content[idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK: pedido de permisos de bateria agregado')
