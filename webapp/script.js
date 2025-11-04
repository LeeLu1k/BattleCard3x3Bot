const tg = window.Telegram.WebApp;
tg.expand();

const user = tg.initDataUnsafe?.user;
const userNameEl = document.getElementById("userName");
const pages = document.querySelectorAll(".page");
const navButtons = document.querySelectorAll(".nav-btn");

if (user) {
    userNameEl.textContent = user.username ? `@${user.username}` : user.first_name;

    // Авторизация
    fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            id: user.id,
            username: user.username || user.first_name
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        renderHeroes(data.player.heroes);
    })
    .catch(err => console.error("Ошибка входа:", err));
}

// Переключение страниц
navButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        const target = btn.dataset.page;
        pages.forEach(p => p.classList.remove("active"));
        document.getElementById(`page-${target}`).classList.add("active");
    });
});

// Рендер списка героев
function renderHeroes(heroes) {
    const list = document.getElementById("heroesList");
    list.innerHTML = "";
    heroes.forEach(h => {
        const div = document.createElement("div");
        div.className = "hero-card";
        div.innerHTML = `
            <img src="https://api.dicebear.com/7.x/pixel-art/png?seed=${h.skin}" alt="${h.name}">
            <p>${h.emoji} ${h.name}</p>
        `;
        list.appendChild(div);
    });
}
