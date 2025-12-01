fetch('/api/tasks/')
.then(res => res.json())
.then(data => console.log(data));