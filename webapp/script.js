const tg = window.Telegram.WebApp;
tg.expand();

const user = tg.initDataUnsafe?.user;
const userNameEl = document.getElementById("userName");
const pages = document.querySelectorAll(".page");
const navButtons = document.querySelectorAll(".nav-btn");

// Проверяем, что Telegram действительно передал данные
if (user) {
    userNameEl.textContent = user.username ? `@${user.username}` : user.first_name;

    // Авторизация на сервере (создание / загрузка игрока)
    fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            id: user.id,
            username: user.username || user.first_name
        })
    })
    .then(res => {
        if (!res.ok) throw new Error("Ошибка сервера");
        return res.json();
    })
    .then(data => {
        console.log("✅ Успешный вход:", data);
        if (data.message) {
            // alert(data.message); // можно убрать если мешает
            console.log(data.message);
        }

        // Если у игрока есть герои — показываем
        if (data.player && data.player.heroes && Array.isArray(data.player.heroes)) {
            renderHeroes(data.player.heroes);
        } else {
            renderHeroes([]);
        }
    })
    .catch(err => {
        console.error("❌ Ошибка входа:", err);
        userNameEl.textContent = "Ошибка загрузки";
        renderHeroes([]);
    });
} else {
    userNameEl.textContent = "Неизвестный игрок";
    renderHeroes([]);
}

// 🔁 Переключение страниц (меню, герои и т.д.)
navButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        const target = btn.dataset.page;
        pages.forEach(p => p.classList.remove("active"));
        const page = document.getElementById(`page-${target}`);
        if (page) page.classList.add("active");
    });
});

// ⚔️ Рендер списка героев (в стиле пиксель-аватаров)
function renderHeroes(heroes = []) {
    const list = document.getElementById("heroesList");
    if (!list) return;

    list.innerHTML = "";

    if (heroes.length === 0) {
        list.innerHTML = `<p style="color:#ccc; font-size:10px;">У тебя пока нет героев 😢<br>Зайди в игру, чтобы получить первого!</p>`;
        return;
    }

    heroes.forEach(h => {
        const div = document.createElement("div");
        div.className = "hero-card";
        div.innerHTML = `
            <img src="https://api.dicebear.com/7.x/pixel-art/png?seed=${h.skin || 'hero'}" alt="${h.name}">
            <p>${h.emoji || '🧙‍♂️'} ${h.name || 'Безымянный'}</p>
        `;
        list.appendChild(div);
    });
}
