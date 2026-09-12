path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'vence pronto' in content:
    print('Ya estaba aplicado, no se modifica nada')
else:
    anchor = 'if(due - 3600000 > Date.now())'
    idx = content.find(anchor)
    if idx == -1:
        raise SystemExit('No se encontro el bloque de 1 hora antes')

    brace_open = content.find('{', idx)
    depth = 0
    i = brace_open
    while i < len(content):
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                break
        i += 1
    insert_pos = i + 1

    extra = (
        "\n  else if(due > Date.now()){\n"
        "    notifications.push({ id: base+3, title:'Tarea importante', "
        "body:`\"${task.title}\" vence pronto`, schedule:{ at: new Date(due) } });\n"
        "  }"
    )
    content = content[:insert_pos] + extra + content[insert_pos:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK: bloque agregado')
