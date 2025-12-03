const token = localStorage.getItem("access");
if(!token) window.location.href = "/login/";

async function loadTasks() {
    const response = await fetch(API + "tasks/", {
        headers: { Authorization: `Bearer ${token}` }
    });

    const data = await response.json();

    const list = taskList;
    list.innerHTML = "";

    data.forEach(task => {
        list.innerHTML += `
            <div class="bg-white p-4 shadow rounded mb-2">
                <h3 class="font-bold">${task.title}</h3>
                <p>${task.description}</p>
                <p class="text-sm text-gray-500">Category: ${task.category}</p>
            </div>
        `;
    });
}

async function createTask() {
    const title = taskTitle.value;
    const description = taskDesc.value;
    const category = taskCategory.value;

    await fetch(API + "tasks/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ title, description, category })
    });

    loadTasks();
}

loadTasks();
