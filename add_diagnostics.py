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
  setTimeout(function(){
    var el = document.getElementById('banner');
    if(!el) return;
    var tieneCapacitor = !!window.Capacitor;
    var tienePlugin = !!(window.Capacitor && Capacitor.Plugins && Capacitor.Plugins.LocalNotifications);
    el.textContent = 'DIAGNOSTICO_CAPACITOR -> Capacitor: ' + (tieneCapacitor ? 'SI' : 'NO') + ' | LocalNotifications: ' + (tienePlugin ? 'SI' : 'NO');
    el.classList.add('show');
    el.style.position = 'sticky';
    el.style.top = '0';
    el.style.zIndex = '999';
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
