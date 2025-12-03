const API = "http://127.0.0.1:8000/api/auth/";

document.getElementById("loginForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(API + "login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh || "");
      window.location.href = "/dashboard/";
    } else {
      alert(data.detail || (data.non_field_errors && data.non_field_errors.join(", ")) || "Login failed");
    }
  } catch (err) {
    alert("Network error");
  }
});
