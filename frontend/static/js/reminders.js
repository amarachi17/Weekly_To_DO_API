const API = "http://127.0.0.1:8000/api/";
const token = localStorage.getItem("access");
if (!token) window.location.href = "/login/";

const reminderList = document.getElementById("reminderList");
const reminderForm = document.getElementById("reminderForm");

reminderForm?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const task = document.getElementById("taskId").value.trim();
  const reminder_at = document.getElementById("reminderTime").value;

  if (!task || !reminder_at) return alert("Provide task id and time");

  try {
    const res = await fetch(API + "reminders/", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
      body: JSON.stringify({ task, reminder_at })
    });

    if (res.ok) {
      loadReminders();
      reminderForm.reset();
    } else {
      const err = await res.json();
      alert(err.detail || JSON.stringify(err));
    }
  } catch {
    alert("Network error");
  }
});

async function loadReminders() {
  try {
    const res = await fetch(API + "reminders/", { headers: { Authorization: `Bearer ${token}` }});
    if (!res.ok) {
      if (res.status === 401) { localStorage.removeItem('access'); window.location.href = "/login/"; }
      return;
    }
    const data = await res.json();
    reminderList.innerHTML = data.map(r => `
      <div class="bg-white p-4 shadow rounded mb-2">
        <p>Task ID: ${r.task}</p>
        <p>Time: ${r.reminder_at}</p>
      </div>
    `).join("");
  } catch {
    alert("Error loading reminders");
  }
}

loadReminders();
