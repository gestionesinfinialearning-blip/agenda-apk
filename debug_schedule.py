import base64

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'PANEL_DEBUG_FIJO'
if marker in content:
    print('Ya estaba aplicado')
else:
    b64 = "KGZ1bmN0aW9uKCl7CiAgdmFyIHBhbmVsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7CiAgcGFuZWwuaWQgPSAnZGVidWdwYW5lbCc7CiAgcGFuZWwuc3R5bGUucG9zaXRpb24gPSAnZml4ZWQnOwogIHBhbmVsLnN0eWxlLnRvcCA9ICcwJzsKICBwYW5lbC5zdHlsZS5sZWZ0ID0gJzAnOwogIHBhbmVsLnN0eWxlLnJpZ2h0ID0gJzAnOwogIHBhbmVsLnN0eWxlLnpJbmRleCA9ICc5OTk5OSc7CiAgcGFuZWwuc3R5bGUuYmFja2dyb3VuZCA9ICdibGFjayc7CiAgcGFuZWwuc3R5bGUuY29sb3IgPSAnbGltZSc7CiAgcGFuZWwuc3R5bGUuZm9udFNpemUgPSAnMTFweCc7CiAgcGFuZWwuc3R5bGUucGFkZGluZyA9ICc2cHgnOwogIHBhbmVsLnN0eWxlLm1heEhlaWdodCA9ICc0MHZoJzsKICBwYW5lbC5zdHlsZS5vdmVyZmxvd1kgPSAnYXV0byc7CiAgcGFuZWwuc3R5bGUud2hpdGVTcGFjZSA9ICdwcmUtd3JhcCc7CiAgZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChwYW5lbCk7CiAgd2luZG93LmRlYnVnTG9nID0gZnVuY3Rpb24obXNnKXsKICAgIHZhciBsaW5lID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7CiAgICBsaW5lLnRleHRDb250ZW50ID0gbmV3IERhdGUoKS50b0xvY2FsZVRpbWVTdHJpbmcoKSArICcgLSAnICsgbXNnOwogICAgcGFuZWwuYXBwZW5kQ2hpbGQobGluZSk7CiAgfTsKICB3aW5kb3cuZGVidWdMb2coJ3BhbmVsIGNhcmdhZG8nKTsKfSkoKTsKCnNjaGVkdWxlTG9jYWxOb3RpZmljYXRpb24gPSBhc3luYyBmdW5jdGlvbih0YXNrKXsKICB0cnl7CiAgICB3aW5kb3cuZGVidWdMb2coJ3NjaGVkdWxlTG9jYWxOb3RpZmljYXRpb24gbGxhbWFkbyBwYXJhOiAnICsgdGFzay50aXRsZSk7CiAgICB2YXIgTE4gPSBnZXRMTigpOwogICAgaWYoIUxOKXsgd2luZG93LmRlYnVnTG9nKCdOTyBoYXkgcGx1Z2luIExOJyk7IHJldHVybjsgfQogICAgaWYoIXRhc2suaW1wb3J0YW50KXsgd2luZG93LmRlYnVnTG9nKCd0YXJlYSBOTyBlcyBpbXBvcnRhbnRlJyk7IHJldHVybjsgfQogICAgaWYoIXRhc2suZHVlKXsgd2luZG93LmRlYnVnTG9nKCd0YXJlYSBTSU4gZmVjaGEnKTsgcmV0dXJuOyB9CiAgICBpZih0YXNrLmRvbmUpeyB3aW5kb3cuZGVidWdMb2coJ3RhcmVhIHlhIGVzdGEgaGVjaGEnKTsgcmV0dXJuOyB9CiAgICB2YXIgZHVlID0gbmV3IERhdGUodGFzay5kdWUpLmdldFRpbWUoKTsKICAgIHZhciBiYXNlID0gaGFzaElkKHRhc2suaWQpOwogICAgdmFyIG5vdGlmaWNhdGlvbnMgPSBbXTsKICAgIHZhciBub3cgPSBEYXRlLm5vdygpOwogICAgdmFyIHJhbWEgPSAnJzsKICAgIGlmKGR1ZSAtIDg2NDAwMDAwID4gbm93KXsKICAgICAgbm90aWZpY2F0aW9ucy5wdXNoKHsgaWQ6IGJhc2UrMSwgdGl0bGU6J1RhcmVhIGltcG9ydGFudGUnLCBib2R5OiB0YXNrLnRpdGxlICsgJyB2ZW5jZSBlbiBtZW5vcyBkZSAyNCBob3JhcycsIHNjaGVkdWxlOnsgYXQ6IG5ldyBEYXRlKGR1ZS04NjQwMDAwMCkgfSB9KTsKICAgICAgcmFtYSA9ICcyNGgnOwogICAgfQogICAgaWYoZHVlIC0gMzYwMDAwMCA+IG5vdyl7CiAgICAgIG5vdGlmaWNhdGlvbnMucHVzaCh7IGlkOiBiYXNlKzIsIHRpdGxlOidUYXJlYSBpbXBvcnRhbnRlJywgYm9keTogdGFzay50aXRsZSArICcgdmVuY2UgZW4gbWVub3MgZGUgMSBob3JhJywgc2NoZWR1bGU6eyBhdDogbmV3IERhdGUoZHVlLTM2MDAwMDApIH0gfSk7CiAgICAgIHJhbWEgKz0gJysxaCc7CiAgICB9IGVsc2UgaWYoZHVlID4gbm93KXsKICAgICAgbm90aWZpY2F0aW9ucy5wdXNoKHsgaWQ6IGJhc2UrMywgdGl0bGU6J1RhcmVhIGltcG9ydGFudGUnLCBib2R5OiB0YXNrLnRpdGxlICsgJyB2ZW5jZSBwcm9udG8nLCBzY2hlZHVsZTp7IGF0OiBuZXcgRGF0ZShkdWUpIH0gfSk7CiAgICAgIHJhbWEgKz0gJytpbm1lZGlhdGEnOwogICAgfQogICAgd2luZG93LmRlYnVnTG9nKCdyYW1hPScgKyByYW1hICsgJyBkdWU9JyArIG5ldyBEYXRlKGR1ZSkudG9Mb2NhbGVUaW1lU3RyaW5nKCkgKyAnIG5vdz0nICsgbmV3IERhdGUobm93KS50b0xvY2FsZVRpbWVTdHJpbmcoKSArICcgY2FudE5vdGlmcz0nICsgbm90aWZpY2F0aW9ucy5sZW5ndGgpOwogICAgaWYobm90aWZpY2F0aW9ucy5sZW5ndGgpewogICAgICBhd2FpdCBMTi5zY2hlZHVsZSh7IG5vdGlmaWNhdGlvbnM6IG5vdGlmaWNhdGlvbnMgfSk7CiAgICAgIHdpbmRvdy5kZWJ1Z0xvZygnUFJPR1JBTUFETyBPSzogJyArIEpTT04uc3RyaW5naWZ5KG5vdGlmaWNhdGlvbnMubWFwKGZ1bmN0aW9uKG4peyByZXR1cm4ge2lkOm4uaWQsIGF0Om4uc2NoZWR1bGUuYXR9OyB9KSkpOwogICAgfQogIH1jYXRjaChlKXsKICAgIHdpbmRvdy5kZWJ1Z0xvZygnRVJST1I6ICcgKyBlLm1lc3NhZ2UpOwogIH0KfTsK"
    js = base64.b64decode(b64).decode('utf-8')
    patch = "\n<script>\n// PANEL_DEBUG_FIJO\n" + js + "</script>\n"
    idx = content.rfind('</body>')
    if idx == -1:
        content = content + patch
    else:
        content = content[:idx] + patch + content[idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK: panel de debug agregado')  try{
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
