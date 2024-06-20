function toggleCommentSection(albumElement) {
    const commentSection = albumElement.querySelector('.album-comment-section');
    if (commentSection.style.display === 'none' || commentSection.style.display === '') {
        commentSection.style.display = 'block';
    } else {
        commentSection.style.display = 'none';
    }
}
