const API = "http://127.0.0.1:8000/api/";
const token = localStorage.getItem("access");
if (!token) window.location.href = "/login/";

const categoryList = document.getElementById("categoryList");
const categoryForm = document.getElementById("categoryForm");

categoryForm?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("categoryName").value.trim();
  if (!name) return alert("Enter a category name");

  try {
    const res = await fetch(API + "categories/", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
      body: JSON.stringify({ name })
    });
    if (res.ok) {
      loadCategories();
      categoryForm.reset();
    } else {
      const err = await res.json();
      alert(err.detail || JSON.stringify(err));
    }
  } catch {
    alert("Network error");
  }
});

async function loadCategories() {
  try {
    const res = await fetch(API + "categories/", { headers: { Authorization: `Bearer ${token}` }});
    if (!res.ok) {
      if (res.status === 401) { localStorage.removeItem('access'); window.location.href = "/login/"; }
      return;
    }
    const data = await res.json();
    categoryList.innerHTML = data.map(c => `<li class="p-2 border-b">${c.name}</li>`).join("");
  } catch {
    alert("Error loading categories");
  }
}

loadCategories();
