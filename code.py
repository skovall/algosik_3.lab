class Task:
    def __init__(self, task_id, description, priority):
        self.id = task_id
        self.description = description
        self.priority = priority
    
    def __str__(self):
        return f"ID: {self.id} | Приоритет: {self.priority} | Описание: {self.description}"


class TaskQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, task):
        if not isinstance(task, Task):
            raise TypeError("Можно добавить только объекты класса Task.")
        
        for i in range(len(self.queue)):
            if task.priority < self.queue[i].priority:
                self.queue.insert(i, task)
                return
        
        self.queue.append(task)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display_all(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        
        print(f"\nВсего задач: {self.size()}")
        for i, task in enumerate(self.queue, 1):
            print(f"{i}. {task}")

    def get_task_by_priority(self, target_priority):
        if self.is_empty():
            print("Очередь пуста.")
            return []

        found_tasks = []
        for task in self.queue:
            if task.priority == target_priority:
                found_task.appened(task)

        if found_tasks:
            print(f"\nНайдено задач с приоритетом {target_priority}: {len(found_tasks)}.")
            for i, task in enumerate(found_tasks, 1):
                print(f"{i}. {task}")
        else:
            print(f"Задач с приоритетом {target_priority} не найдено.")
        
        return found_tasks
        
def main():
    task_queue = TaskQueue()
    
    task1 = Task(1, "Написать отчет", 2)
    task2 = Task(2, "Проверить код", 1)
    task3 = Task(3, "Выгрузить код", 3)
    task4 = Task(4, "Подключиться к конфе", 4)
    task5 = Task(5, "Успешно защититься", 5)
    
    task_queue.enqueue(task1)
    task_queue.enqueue(task2)
    task_queue.enqueue(task3)
    task_queue.enqueue(task4)
    task_queue.enqueue(task5)
    
    print("\nВывод всех задач")
    task_queue.display_all()
    
    print("\nПроверка isEmpty")
    print(f"Очередь пуста: {task_queue.is_empty()}")
    print(f"Размер очереди: {task_queue.size()}")
    
    print("\nПросмотр первой задачи (front)")
    first = task_queue.front()
    if first:
        print(f"Первая задача: {first}")
    
    print("\nИзвлечение задач (dequeue)")
    while not task_queue.is_empty():
        task = task_queue.dequeue()
        print(f"Извлечено: {task}")
    
    print("\nПроверка после извлечения")
    print(f"Очередь пуста: {task_queue.is_empty()}")
    task_queue.display_all()
    
    print("\nПопытка извлечь из пустой очереди")
    result = task_queue.dequeue()
    if result is None:
        print("Очередь пуста, извлечение невозможно.")
    
    print("\nПроверка front на пустой очереди")
    result = task_queue.front()
    if result is None:
        print("Очередь пуста, нет первой задачи.")

if __name__ == "__main__":
    main()
