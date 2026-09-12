path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'ALERT_SCHEDULE_DEBUG'
if marker in content:
    print('Ya estaba aplicado')
else:
    patch = """
<script>
// ALERT_SCHEDULE_DEBUG
scheduleLocalNotification = async function(task){
  function log(msg){ alert('DEBUG: ' + msg); }
  try{
    var LN = getLN();
    if(!LN){ log('no hay plugin LN'); return; }
    if(!task.important){ log('tarea no es importante'); return; }
    if(!task.due){ log('tarea sin fecha'); return; }
    if(task.done){ log('tarea ya hecha'); return; }
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
    log('rama=' + rama + ' | due=' + new Date(due).toLocaleTimeString() + ' | now=' + new Date(now).toLocaleTimeString() + ' | notifs=' + notifications.length);
    if(notifications.length){
      await LN.schedule({ notifications: notifications });
      log('programado OK, id/at=' + JSON.stringify(notifications.map(function(n){ return {id:n.id, at:n.schedule.at}; })));
    }
  }catch(e){
    log('ERROR: ' + e.message);
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
    print('OK: alert debug agregado')
