path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'DEBUG_SCHEDULE_OVERRIDE'
if marker in content:
    print('Ya estaba aplicado')
else:
    patch = """
<script>
scheduleLocalNotification = async function(task){
  var el = document.getElementById('banner');
  function log(msg){
    if(el){ el.textContent = msg; el.classList.add('show'); el.style.position='sticky'; el.style.top='0'; el.style.zIndex='999'; el.style.fontSize='11px'; }
  }
  try{
    var LN = getLN();
    if(!LN){ log('DEBUG: no hay plugin LN'); return; }
    if(!task.important){ log('DEBUG: tarea no es importante'); return; }
    if(!task.due){ log('DEBUG: tarea sin fecha'); return; }
    if(task.done){ log('DEBUG: tarea ya hecha'); return; }
    var due = new Date(task.due).getTime();
    var base = hashId(task.id);
    var notifications = [];
    var now = Date.now();
    var rama = '';
    if(due - 86400000 > now){
      notifications.push({ id: base+1, title:'Tarea importante', body: task.title + ' vence en menos de 24 horas', schedule:{ at: new Date(due-86400000) } });
      rama = '24h';
    }
    if(due - 3600000 > now){
      notifications.push({ id: base+2, title:'Tarea importante', body: task.title + ' vence en menos de 1 hora', schedule:{ at: new Date(due-3600000) } });
      rama += '+1h';
    } else if(due > now){
      notifications.push({ id: base+3, title:'Tarea importante', body: task.title + ' vence pronto', schedule:{ at: new Date(due) } });
      rama += '+inmediata';
    }
    log('DEBUG rama=' + rama + ' due=' + new Date(due).toLocaleTimeString() + ' now=' + new Date(now).toLocaleTimeString() + ' notifs=' + notifications.length);
    if(notifications.length){
      await LN.schedule({ notifications: notifications });
      log('DEBUG programado OK: ' + JSON.stringify(notifications.map(function(n){ return {id:n.id, at:n.schedule.at}; })));
    }
  }catch(e){
    log('DEBUG ERROR: ' + e.message);
  }
};
</script>
"""
    idx = content.rfind('</body>')
    if idx == -1:
        content = content + patch
    else:
        content = content[:idx] + patch + content[idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK: debug schedule agregado')
