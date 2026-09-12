path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'PANEL_DEBUG_FIJO'
if marker in content:
    print('Ya estaba aplicado')
else:
    patch = """
<script>
// PANEL_DEBUG_FIJO
(function(){
  var panel = document.createElement('div');
  panel.id = 'debugpanel';
  panel.style.position = 'fixed';
  panel.style.top = '0';
  panel.style.left = '0';
  panel.style.right = '0';
  panel.style.zIndex = '99999';
  panel.style.background = 'black';
  panel.style.color = 'lime';
  panel.style.fontSize = '11px';
  panel.style.padding = '6px';
  panel.style.maxHeight = '40vh';
  panel.style.overflowY = 'auto';
  panel.style.whiteSpace = 'pre-wrap';
  document.body.appendChild(panel);
  window.debugLog = function(msg){
    var line = document.createElement('div');
    line.textContent = new Date().toLocaleTimeString() + ' - ' + msg;
    panel.appendChild(line);
  };
  window.debugLog('panel cargado');
})();

scheduleLocalNotification = async function(task){
  try{
    window.debugLog('scheduleLocalNotification llamado para: ' + task.title);
    var LN = getLN();
    if(!LN){ window.debugLog('NO hay plugin LN'); return; }
    if(!task.important){ window.debugLog('tarea NO es importante'); return; }
    if(!task.due){ window.debugLog('tarea SIN fecha'); return; }
    if(task.done){ window.debugLog('tarea ya esta hecha'); return; }
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
    window.debugLog('rama=' + rama + ' due=' + new Date(due).toLocaleTimeString() + ' now=' + new Date(now).toLocaleTimeString() + ' cantNotifs=' + notifications.length);
    if(notifications.length){
      await LN.schedule({ notifications: notifications });
      window.debugLog('PROGRAMADO OK: ' + JSON.stringify(notifications.map(function(n){ return {id:n.id, at:n.schedule.at}; })));
    }
  }catch(e){
    window.debugLog('ERROR: ' + e.message);
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
    print('OK: panel de debug agregado')    if(notifications.length){
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
