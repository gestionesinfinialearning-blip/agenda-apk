path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'vence pronto'
if marker in content:
    print('Ya estaba aplicado, no se modifica nada')
else:
    patch = """
<script>
scheduleLocalNotification = async function(task){
  const LN = getLN();
  if(!LN || !task.important || !task.due || task.done) return;
  const due = new Date(task.due).getTime();
  const base = hashId(task.id);
  const notifications = [];
  if(due - 86400000 > Date.now()){
    notifications.push({ id: base+1, title:'Tarea importante', body:`"${task.title}" vence en menos de 24 horas`, schedule:{ at: new Date(due-86400000) } });
  }
  if(due - 3600000 > Date.now()){
    notifications.push({ id: base+2, title:'Tarea importante', body:`"${task.title}" vence en menos de 1 hora`, schedule:{ at: new Date(due-3600000) } });
  } else if(due > Date.now()){
    notifications.push({ id: base+3, title:'Tarea importante', body:`"${task.title}" vence pronto`, schedule:{ at: new Date(due) } });
  }
  if(notifications.length){
    try{ await LN.schedule({ notifications }); }catch(e){ console.error('No se pudo programar el aviso', e); }
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
    print('OK: parche agregado')
