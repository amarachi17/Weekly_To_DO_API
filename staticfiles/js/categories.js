const API = "http://127.0.0.1:8000/api/";
const token = localStorage.getItem("access");
if(!token) window.location.href = "/login/";

async function loadCategories() {
    const response = await fetch(API + "categories/", {
        headers: { Authorization: `Bearer ${token}` }
    });

    const data = await response.json();

    const list = document.getElementById("categoryList");
    list.innerHTML = "";

    data.forEach(cat => {
        list.innerHTML += `<li class="p-2 border-b">${cat.name}</li>`;
    });
}

async function createCategory() {
    const name = document.getElementById("categoryName").value;

    await fetch(API + "categories/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ name })
    });

    loadCategories();
}

loadCategories();
