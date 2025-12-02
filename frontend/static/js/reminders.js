async function loadReminders() {
    const response = await fetch(API + "reminders/", {
        headers: { Authorization: `Bearer ${token}` }
    });

    const data = await response.json();

    const list = document.getElementById("reminderList");
    list.innerHTML = "";

    data.forEach(task => {
        list.innerHTML += `
        <div class="bg-white p-4 shadow rounded mb-2">
            <p> Task ID ${item.task} </p>
            <p> Time: ${item.time} </p>

        </div>
        `;
    });

}

async function createReminder() {
    const task = taskId.value;
    const time = reminderTime.value;

    await fetch(API + "reminders/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ task, time })
    });

    loadReminders();
}

loadReminders();
