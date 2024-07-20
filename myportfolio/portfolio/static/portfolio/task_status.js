document.addEventListener('DOMContentLoaded', function() {
    const taskId = document.querySelector('p').innerText.split(': ')[1];
    if (taskId) {
        fetch(`/portfolio/get_task_status/${taskId}/`)
            .then(response => response.json())
            .then(data => {
                const statusElement = document.createElement('p');
                statusElement.textContent = `Task Status: ${data.status}`;
                if (data.status === 'success') {
                    const outputElement = document.createElement('pre');
                    outputElement.textContent = `Output:\n${data.output}`;
                    document.body.appendChild(outputElement);
                } else if (data.status === 'failure') {
                    const errorElement = document.createElement('p');
                    errorElement.textContent = `Error: ${data.message}`;
                    document.body.appendChild(errorElement);
                }
                document.body.appendChild(statusElement);
            });
    }
});
