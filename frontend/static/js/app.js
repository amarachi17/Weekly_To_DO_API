document.addEventListener('DOMContentLoaded', loadTasks);

function loadTasks() {
    fetch('/api/tasks/')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('taskList');
            list.innerHTML = '';

            data.forEach(task => {
                let item = document.createElement('div');
                item.className = 'task-item';
                item.innerHTML = `
                    <h3> ${task.title} </h3>
                    <p> ${task.content} </p>
                `;
                list.appendChild(item);
            });

        });
}

function createTasl() {
    const title = document.getElementById('taskTitle').value;
    const content = document.getElementById('taskContent').value;

    fetch('api/tasks/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            content: content
        })
    })
    .then(() =>{
        loadTasks();
        document.getElementById('taskTitle').value = '';
        document.getElementById('taskContent').value = '';
    })
}