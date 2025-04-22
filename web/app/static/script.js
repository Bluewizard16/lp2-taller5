document.getElementById("login-form").addEventListener("submit", async function (event) {
    event.preventDefault(); // Evitar que el formulario recargue la página

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("/login-form", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            // Redirigir al usuario a la página principal si el login es exitoso
            window.location.href = "/";
        } else {
            // Mostrar un mensaje de error si las credenciales son incorrectas
            const errorMessage = document.getElementById("error-message");
            errorMessage.style.display = "block";
            errorMessage.textContent = "Credenciales incorrectas. Inténtalo de nuevo.";
        }
    } catch (error) {
        console.error("Error al realizar la solicitud:", error);
    }
});