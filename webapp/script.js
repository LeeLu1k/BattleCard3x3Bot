const tg = window.Telegram.WebApp;
tg.expand();

const user = tg.initDataUnsafe?.user;

if (user) {
    document.getElementById("userName").textContent =
        user.username ? `@${user.username}` : user.first_name;

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
        console.log("Player data:", data);
        alert(data.message);

        // Показываем аватар
        const seed = user.id;
        document.getElementById("avatar").src =
            `https://api.dicebear.com/7.x/pixel-art/png?seed=${seed}`;
    })
    .catch(err => console.error("Ошибка входа:", err));
}
