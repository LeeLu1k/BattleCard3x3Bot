const tg = window.Telegram.WebApp;
tg.expand();

const user = tg.initDataUnsafe?.user;
const avatarImg = document.getElementById("avatar");

// Показываем ник
if (user) {
    const name = user.username
        ? `@${user.username}`
        : `${user.first_name || ''} ${user.last_name || ''}`.trim();
    document.getElementById("userName").textContent = name || "Игрок";

    // Генерируем пиксельный аватар (на основе Telegram ID, чтобы был уникальный)
    const seed = user.id || Math.random().toString(36).substring(2);
    avatarImg.src = `https://api.dicebear.com/7.x/pixel-art/png?seed=${seed}`;
} else {
    document.getElementById("userName").textContent = "Гость";
    avatarImg.src = `https://api.dicebear.com/7.x/pixel-art/png?seed=random`;
}

document.getElementById("startGame").addEventListener("click", () => {
    tg.sendData(JSON.stringify({ action: "start_game" }));
});
