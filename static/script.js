function toggleCommentSection(albumElement) {
    const commentSection = albumElement.querySelector('.album-comment-section');
    const allCommentSections = document.querySelectorAll('.album-comment-section');

    allCommentSections.forEach(section => {
        if (section !== commentSection && section.classList.contains('expanded')) {
            section.classList.remove('expanded');
        }
    });

    if (commentSection.classList.contains('expanded')) {
        commentSection.classList.remove('expanded');
    } else {
        commentSection.classList.add('expanded');
    }
}
