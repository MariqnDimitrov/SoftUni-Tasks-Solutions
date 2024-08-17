function attachEvents() {
    let btnLoadPostsElement = document.getElementById('btnLoadPosts');
    let postsSelectElement = document.getElementById('posts');
    let btnViewPostElement = document.getElementById('btnViewPost');
    let postBodyElement = document.getElementById('post-body');
    let postTitleElement = document.getElementById('post-title');
    btnLoadPostsElement.addEventListener('click', () => {
        fetch('http://localhost:3030/jsonstore/blog/posts')
        .then(res => res.json())
        .then(data => {
            Object.values(data)
                .forEach(element => {
                    let dataOption = document.createElement('option');
                    dataOption.value = element.id;
                    dataOption.text = element.title;
                    postsSelectElement.appendChild(dataOption);
                });
        });
    });

    btnViewPostElement.addEventListener('click', () => {
        fetch(`http://localhost:3030/jsonstore/blog/posts/${postsSelectElement.value}`)
        .then(res => res.json())
        .then(data =>{
            postBodyElement.textContent = data.body;
            postTitleElement.textContent = data.title;      
        })
        fetch(`http://localhost:3030/jsonstore/blog/comments`)
        .then(res => res.json())
        .then(data => {
            Object.values(data)
            .filter(id => id.postId === postsSelectElement.value)
            .forEach(comment =>{
                const comments = document.createElement('li');
                comments.id = comment.id;
                comments.textContent = comment.text;
                let postCommentsElement = document.getElementById('post-comments');
                postCommentsElement.appendChild(comments);
            });
        });
    });



}

attachEvents();