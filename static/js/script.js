const toggleBtn = document.getElementById('darkModeToggle');
const htmlElement = document.documentElement;


const currentTheme = localStorage.getItem('theme') || 'light';
htmlElement.setAttribute('data-bs-theme', currentTheme);

toggleBtn.addEventListener('click', () => {
    const newTheme = htmlElement.getAttribute('data-bs-theme') === 'light' ? 'dark' : 'light';
    htmlElement.setAttribute('data-bs-theme', newTheme);
    localStorage.setItem('theme', newTheme);
});