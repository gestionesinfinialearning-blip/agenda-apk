path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'DIAGNOSTICO_CAPACITOR'
if marker in content:
    print('Ya estaba aplicado')
else:
    patch = """
<script>
window.addEventListener('load', function(){
  if(window.Capacitor){
    var elBtn = document.getElementById('notifSetup');
    if(elBtn) elBtn.style.display = 'none';
  }
  setTimeout(async function(){
    var el = document.getElementById('banner');
    if(!el) return;
    var tieneCapacitor = !!window.Capacitor;
    var LN = (window.Capacitor && Capacitor.Plugins && Capacitor.Plugins.LocalNotifications) || null;
    var texto = 'Capacitor: ' + (tieneCapacitor ? 'SI' : 'NO') + ' | Plugin: ' + (LN ? 'SI' : 'NO');
    if(LN){
      try{
        var perm = await LN.checkPermissions();
        texto += ' | Permiso: ' + JSON.stringify(perm);
        var pedido = await LN.requestPermissions();
        texto += ' | Tras pedir: ' + JSON.stringify(pedido);
        await LN.schedule({ notifications: [{ id: 999999, title: 'Prueba directa', body: 'Si ves esto, el sistema funciona', schedule: { at: new Date(Date.now() + 15000) } }] });
        texto += ' | Prueba programada para 15s';
      }catch(e){
        texto += ' | ERROR: ' + e.message;
      }
    }
    el.textContent = texto;
    el.classList.add('show');
    el.style.position = 'sticky';
    el.style.top = '0';
    el.style.zIndex = '999';
    el.style.fontSize = '12px';
  }, 1500);
});
</script>
"""
    idx = content.rfind('</body>')
    if idx == -1:
        content = content + patch
    else:
        content = content[:idx] + patch + content[idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK: diagnostico agregado')
