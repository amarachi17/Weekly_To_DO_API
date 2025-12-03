const API = "http://127.0.0.1:8000/api/auth/";

document.getElementById("registerForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(API + "register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
      alert("Account created successfully! Please login.");
      window.location.href = "/login/";
    } else {
      alert(data.detail || JSON.stringify(data) || "Registration failed");
    }
  } catch {
    alert("Network error");
  }
});
