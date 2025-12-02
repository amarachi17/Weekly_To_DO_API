const API = "http://127.0.0.1:8000/api/"; 

document.getElementById("loginForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = email.value;
    const password = password.value;

    const response = await fetch(API + "login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("token", data.access);
        window.location.href = "/dashbord/";
    } else {
        alert(data.detail || "Login failed");
    }
});