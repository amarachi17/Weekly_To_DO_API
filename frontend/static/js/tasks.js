const API = "http://127.0.0.1:8000/api/";
const token = localStorage.getItem("access");
if (!token) window.location.href = "/login/";

const taskList = document.getElementById("taskList");
const taskForm = document.getElementById("taskForm");

taskForm?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("taskTitle").value.trim();
  const description = document.getElementById("taskDescription").value.trim();
  const category = document.getElementById("taskCategory").value.trim() || null;

  try {
    const res = await fetch(API + "tasks/", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
      body: JSON.stringify({ title, description, category })
    });

    if (res.ok) {
      loadTasks();
      taskForm.reset();
    } else {
      const err = await res.json();
      alert(err.detail || JSON.stringify(err));
    }
  } catch {
    alert("Network error");
  }
});

async function loadTasks() {
  try {
    const res = await fetch(API + "tasks/", { headers: { Authorization: `Bearer ${token}` }});
    if (!res.ok) {
      if (res.status === 401) { localStorage.removeItem('access'); window.location.href = "/login/"; }
      return;
    }
    const data = await res.json();
    taskList.innerHTML = data.map(t => `
      <div class="bg-white p-4 shadow rounded mb-2">
        <h3 class="font-bold">${t.title}</h3>
        <p>${t.description}</p>
        <p class="text-sm text-gray-500">Category: ${t.category || 'None'}</p>
      </div>
    `).join("");
  } catch {
    alert("Error loading tasks");
  }
}

loadTasks();
