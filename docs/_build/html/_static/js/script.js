// override ctrl + f command
document.addEventListener('keydown', function(e) {
    if (e.keyCode === 70 && e.ctrlKey) {
        e.preventDefault();
        document.getElementById('search-input').focus();
    }
});