const token = localStorage.getItem("access");
if(!token) window.location.href = "/login/";

async function loadReminders() {
    const response = await fetch(API + "reminders/", {
        headers: { Authorization: `Bearer ${token}` }
    });

    const data = await response.json();

    const list = reminderList;
    list.innerHTML = "";

    data.forEach(item => {
        list.innerHTML += `
        <div class="bg-white p-4 shadow rounded mb-2">
            <p> Task ID ${item.task} </p>
            <p> Time: ${item.reminder_at} </p>

        </div>
        `;
    });

}

async function createReminder() {
    const task = taskId.value;
    const reminder_at = reminderTime.value;

    await fetch(API + "reminders/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ task, reminder_at })
    });

    loadReminders();
}

loadReminders();
