from todo import TodoList

td = TodoList('main')

while True:
    cmd = input("CMD:>> ")
    if cmd == 'add':
        task = input('Your task:>> ')
        td.add_task(task)
        print("Task added!")
    if cmd == 'show':
        td.draw_tasks()
    if cmd == 'rm':
        n = int(input('Task number:>> '))
        td.remove_task(n)
        print("Task removed!")