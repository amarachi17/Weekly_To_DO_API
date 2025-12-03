const form = document.getElementById("loginForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const res = await fetch("/api/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        })
    });

    if (res.ok) {
        const data = await res.json();
        localStorage.setItem("access", data.access);
        localStorage.setItem("refresh", data.refresh);

        // After login → Go to Dashboard
        window.location.href = "/dashboard/";
    } else {
        alert("Invalid credentials");
    }
});
