const API_URL = "https://sql-injection-detector-zyq1.onrender.com";

// Get references to form elements
const loginForm = document.getElementById("loginForm");
const signupForm = document.getElementById("signupForm");

// Get references to tab buttons
const loginTab = document.getElementById("loginTab");
const signupTab = document.getElementById("signupTab");

// Switch to login form view when login tab is clicked
loginTab.onclick = () => {
    loginForm.classList.add("active");
    signupForm.classList.remove("active");
    loginTab.classList.add("active");
    signupTab.classList.remove("active");
};

// Switch to signup form view when signup tab is clicked
signupTab.onclick = () => {
    signupForm.classList.add("active");
    loginForm.classList.remove("active");
    signupTab.classList.add("active");
    loginTab.classList.remove("active");
};

// Handle signup form submission
signupForm.onsubmit = async (e) => {
    e.preventDefault(); // Prevent page reload

    // Get username and password from input fields
    const username = document.getElementById("signupUsername").value;
    const password = document.getElementById("signupPassword").value;
    const msg = document.getElementById("signupMessage");

    // Send POST request to /register endpoint
    const response = await fetch(`${API_URL}/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    // Parse response and show feedback message
    const data = await response.json();
    msg.textContent = data.message || data.detail;
    msg.className = "message " + (response.ok ? "success" : "error");
};

// Handle login form submission
loginForm.onsubmit = async (e) => {
    e.preventDefault(); // Prevent page reload

    // Get username, password, and capability code from input fields
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;
    const x_code = document.getElementById("capabilityCode").value;
    const msg = document.getElementById("loginMessage");

    // Send POST request to /login endpoint with capability code header
    const response = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "x-code": x_code
        },
        body: JSON.stringify({ username, password })
    });

    // Parse response and show feedback message
    const data = await response.json();
    msg.textContent = data.message || data.detail;
    msg.className = "message " + (response.ok ? "success" : "error");
};
