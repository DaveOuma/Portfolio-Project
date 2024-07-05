document.addEventListener("DOMContentLoaded", function() {
    var taskId = document.getElementById("task-id").innerText;
    var interval = setInterval(function() {
        fetch(`/get_task_status/${taskId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    document.getElementById("output").innerText = data.output;
                    clearInterval(interval);
                } else if (data.status === 'failure') {
                    document.getElementById("output").innerText = data.message;
                    clearInterval(interval);
                }
            });
    }, 1000);
});