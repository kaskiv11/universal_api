function loadTask(){
    fetch('/api/tasks')
        .then(response=> response.json())
        .then(data => {
            const taskDiv = document.getElementById("tasks");
            taskDiv.innerText = "";
            data.tasks.forEach(task=> {
                const taskElement = document.createElement('div');
                taskElement.innerHTML = `
                    <h3>${task.title}</h3>
                    <p>${task.description}</p>
                    <p>Completed: ${task.done ? 'YES' : 'NO'}</p>
                `;
                taskDiv.appendChild(taskElement);
            });
        })
        .catch(error => console.error("Error loading tasks:", error))
}


document.getElementById("taskForm").addEventListener("submit", function (event){
    event.preventDefault();

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    fetch('/api/tasks',{
        method: "POST",
        headers:{
          "Content-Type": 'application/json'
        },
        body: JSON.stringify({title, description })
    })
        .then(response => response.json())
        .then(task => {
            loadTask();
            document.getElementById('taskForm').reset();
        })
        .catch(error => console.error("Error adding task:", error))


});

loadTask();
