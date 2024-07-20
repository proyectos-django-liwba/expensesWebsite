document.addEventListener('DOMContentLoaded', function () {
    const formLogin = document.getElementById('form-login');

    formLogin.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(this);

        // Convierte FormData a un objeto
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Enviar la petición al endpoint de la API
        fetch('http://localhost:8000/authentication/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {
                console.log('Response:', result);
                console.log(result.errors.length)

                if (result.errors.length > 0) {
                    // Mostrar los errores en el formulario
                    handleValidationErrors(result.errors);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });

    });
});

//validación de formulario de login
function handleValidationErrors(errors) {
    errors.forEach(error => {
        const fieldContainer = document.getElementById(`${error.field}_container`);
        const input = fieldContainer.querySelector('input');
        const feedback = fieldContainer.querySelector('.feedback');

        input.classList.add('border-1', 'border-danger');
        feedback.innerHTML = error.error;
    });

    setTimeout(() => {
        errors.forEach(error => {
            const fieldContainer = document.getElementById(`${error.field}_container`);
            const input = fieldContainer.querySelector('input');
            const feedback = fieldContainer.querySelector('.feedback');

            input.classList.remove('border-1', 'border-danger');
            feedback.innerHTML = '';
        });
    }, 2000);
}