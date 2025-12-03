const API = "http://127.0.0.1:8000/api/"; 

document.getElementById("loginForm")?.addEventListener("submit", authenticateUser);

async function authenticateUser(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${API}auth/login/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: email,
                password: password
            }),
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("access", data.access);
            window.location.href = "/dashboard/";
        } else {
            alert(data.detail || "Invalid login credentials");
        }

    } catch (error) {
        alert("Network error");
    }
}