const API = "http://127.0.0.1:8000/api/";

document.getElementById("registerForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(API + "register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, username, password })
        });

        const data = await response.json();
        console.log("REGISTER RESPONSE:", data);

        if (response.ok) {
            alert("Account created successfully!");
            window.location.href = "/login/";
        } else {
            alert(data.detail || "Registration failed");
        }

    } catch (error) {
        console.log("REGISTER ERROR:", error);
        alert("Unable to register. Check your network or server.");
    }
});
